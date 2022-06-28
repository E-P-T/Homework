import json
import logging
import re
from typing import Optional

from bs4 import BeautifulSoup
from bs4.element import PageElement, ResultSet
import requests

from .helpers import validate_method_args, is_number
from .rss_classes import Item, Element, ElementType, ElementCollection


class RSSException(Exception):
    def __init__(self, message, is_logged):
        super().__init__(message)

        self.is_logged = is_logged


class RSSParser:
    """
    This is a class which combines data and methods regarding the parsing of an RSS.
    """

    def __init__(self):
        self.parsed_items: Optional[list[Item]] = None
        self.soup = None
        logging.info('RSS parser is created')

    def request_soup(self, url: str) -> None:
        """
        This function requests `url` and creates a BeautifulSoup object with its content.
        :return: A bs4 soup object to parse xml.
        """
        if not url:
            logging.error('RSS URL must be provided!')
            raise RSSException('Argument url must be of type str.', is_logged=True)
        if not re.match(r'(https?://[^\s"<]+)', url):
            logging.error('Invalid RSS URL was provided!')
            raise RSSException('Argument provided was not a valid web url.', is_logged=True)
        req = requests.get(url)
        logging.info('RSS is requested from given URL')
        self.soup = BeautifulSoup(req.content, features='xml')

    @property
    def feed_title(self) -> str:
        """
        :return: RSS Title
        """
        return self.soup.title.string

    def items(self, limit: Optional[str | int] = None) -> ResultSet:
        """
        This function retrieves all items from an RSS.
        :return: An object containing all raw items.
        """
        if limit is None:
            logging.info('Getting all items from feed')
            return self.soup.findAll('item', limit=limit)
        if not is_number(limit):
            logging.error('RSS parser limit was non-number!')
            raise RSSException('Non-number limit was passed.', is_logged=True)
        if float(limit) % 1:
            logging.error('RSS parser limit passed was not an integer!')
            raise RSSException('Non-integer limit was passed.', is_logged=True)
        limit = int(limit)
        if limit <= 0:
            logging.error('RSS parser limit passed was not a positive integer!')
            raise RSSException('Non-positive limit was passed.', is_logged=True)
        logging.info(f'Getting all items from feed until limit of {limit} item(s) is reached')

        return self.soup.findAll('item', limit=limit)

    @validate_method_args
    def _parse_item(self, item: PageElement) -> Item:
        """
        This function parses a PageElement with its title, date, link, media and description into an Item object.
        :param item: A PageElement to be parsed into an Item.
        :return: A parsed Item.
        """
        title = self._parse_title(item)
        date = self._parse_date(item)
        link = self._parse_link(item)
        media = self._parse_media(item)
        description = self._parse_description(item)
        parsed_item = Item(title=title, date=date, link=link, description=description, media_links=media)
        logging.info(f'Finished parsing item with title: {parsed_item.title}')

        return parsed_item

    @validate_method_args
    def parse_items(self, items: ResultSet) -> None:
        """
        This function parses all given items and assigns them to a class attribute.
        :param items: A ResultSet object with raw items from a rss.
        """
        self.parsed_items = [self._parse_item(item) for item in items]

    @staticmethod
    @validate_method_args
    def _parse_title(item: PageElement) -> Element:
        """
        This function parses the title of a page element and returns it as an Element object.
        :param item: An item from which to get the title.
        :return: An Element object with the value of the title.
        """
        title_elem = Element(ElementType.TITLE)
        title_elem.value = item.title.string.strip()
        logging.info(f'Got item\'s title: {title_elem.value}')
        if not title_elem.value:
            logging.info('Title was not found')
        return title_elem

    @staticmethod
    @validate_method_args
    def _parse_date(item: PageElement) -> Element:
        """
        This function parses the date of a page element and returns it as an Element object.
        :param item: An item from which to get the date.
        :return: An Element object with the value of the date.
        """
        date_elem = Element(ElementType.PUB_DATE)
        date_elem.value = item.pubDate.string
        logging.info(f'Got item\'s publish date: {date_elem.value}')
        if not date_elem.value:
            logging.info('Publish date was not found')
        return date_elem

    @staticmethod
    @validate_method_args
    def _parse_link(item: PageElement) -> Element:
        """
        This function parses the link of a page element and returns it as an Element object.
        :param item: An item from which to get the link.
        :return: An Element object with the value of the link.
        """
        link_elem = Element(ElementType.LINK)
        link_elem.value = item.link.string
        logging.info(f'Got item\'s link: {link_elem.value}')
        if not link_elem.value:
            logging.info('Link was not found')
        return link_elem

    @staticmethod
    @validate_method_args
    def _parse_media(item: PageElement) -> ElementCollection:
        """
        This function takes a PageElement object and returns an ElementCollection of media URLs.
        :param item: An item from which to get the media links.
        :return: An ElementCollection object with the value of media links.
        """
        media_urls = re.findall(r'(https?://[^\s"<]+)', str(item))
        media_collection = None
        if media_urls:
            media_urls = set(map(lambda x: Element(ElementType.MEDIA, x), media_urls))
            media_collection = ElementCollection(ElementType.MEDIA, list(media_urls))
            logging.info(f'Got item\'s media urls, {len(media_collection)} found.')
        if not media_collection:
            logging.info('Media was not found')
        return media_collection

    @staticmethod
    @validate_method_args
    def _parse_description(item: PageElement) -> Element:
        """
        This function parses the description of a page element and returns it as an Element object.
        :param item: An item from which to get the description.
        :return: An Element object with the value of the description.
        """
        desc_elem = Element(ElementType.DESCRIPTION)
        if getattr(item, 'description'):
            desc_elem.value = re.sub('<[^>]*>', '', item.description.text)
            logging.info(f'Got item\'s description: {desc_elem.value}')
        if not desc_elem.value:
            logging.info('Description was not found')
        return desc_elem

    def json_results(self) -> str:
        """
        This function returns a JSON object representation of an RSS feed with the following fields:
            - feed_title: The title of the RSS feed.
            - items: A list of parsed items from the RSS feed.

        :return: A representation of an RSS feed.
        """
        json_dict = {
            'feed_title': self.feed_title,
            'items': [item.value for item in self.parsed_items]
        }
        logging.info('Returning results to the user in JSON format')
        return json.dumps(json_dict, indent=2)
