import logging
import os.path
import pickle
import re
import sys
from typing import Optional

from bs4 import BeautifulSoup
from bs4.element import PageElement, ResultSet
import requests
from dateutil import parser
from dateutil.parser import ParserError

from .helpers import validate_method_args, validate_limit, validate_url
from .rss_classes import Item, Element, ElementType, ElementCollection, RSSCache, Feed, RSSException


class RSSParser:
    """
    This is a class which combines data and methods regarding the parsing of an RSS.
    """

    def __init__(self):
        self.url = None
        self.parsed_items: Optional[list[Item]] = None
        self.soup = None
        self._title = None
        self.rss_cache = CacheReader()
        logging.info('RSS parser is created')

    def request_soup(self, url: str) -> None:
        """
        This function requests `url` and creates a BeautifulSoup object with its content.
        :return: A bs4 soup object to parse xml.
        """
        if not url:
            logging.error('RSS URL must be provided!')
            raise RSSException('Argument url must be of type str.', is_logged=True)
        validate_url(url)
        self.url = url
        req = requests.get(url)
        logging.info('RSS is requested from given URL')
        self.soup = BeautifulSoup(req.content, features='xml')

    @property
    def feed_title(self) -> str:
        """
        :return: RSS Title
        """
        return self._title if self._title else self.soup.title.string

    @feed_title.setter
    def feed_title(self, value):
        self._title = value

    def items(self, limit: Optional[str] = None) -> ResultSet:
        """
        This function retrieves all items from an RSS.
        :return: An object containing all raw items.
        """
        if limit is None:
            logging.info('Getting all items from feed')
            return self.soup.findAll('item', limit=limit)
        limit = validate_limit(limit)

        return self.soup.findAll('item', limit=limit)

    def parse_items_by_date(self, date: str, url: Optional[str], limit: Optional[str]) -> None:
        """
        This function checks the cache for all feeds that match the given date and URL,
        if no URL is provided it will check all feeds. It will add matching items until the limit is reaching,
        if no limit is provided it will retrieve all items.
        :param date:str: Date in the format of yymmdd.
        :param url:Optional[str]: The url of the rss feed to be matched.
        :param limit:Optional[str]: Limit the number of items to be retrieved.
        """
        if len(date) != 8:
            logging.error('The length of parameter --date should be 8 characters long!')
            raise RSSException('Date provided was not 8 characters', is_logged=True)
        try:
            vis_date = parser.parse(date).strftime('%d/%m/%Y')
            print(vis_date)
        except ParserError:
            logging.error('Faulty date was provided!')
            raise RSSException('Date was not matching following format "yymmdd".', is_logged=True)

        current_cache = self.rss_cache.cache
        feed_list = []
        for feed in current_cache.rss_feeds:
            if url and url != feed.url:
                continue
            for item in feed.items:
                item_date = parser.parse(item.date.value).strftime('%Y%m%d')
                if item_date == date:
                    feed_list.append(item)
        feed_str = ''
        if url:
            validate_url(url)
            feed_str += f', and {url} URL'
        if limit:
            limit = validate_limit(limit)
            feed_str += f', and  limit of {limit}'
        else:
            limit = len(feed_list)
        self.feed_title = f'News fetched from cache by - {vis_date} Date{feed_str}.'
        self.parsed_items = feed_list[:limit]
        logging.info(f'Parsed items from cache with following filters Date: {vis_date}{feed_str}')

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
        self.rss_cache.cache_results(self.feed)

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
        date_elem.value = parser.parse(date_elem.value).strftime('%Y-%m-%d %H:%M:%S')
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
        The json_results function returns a JSON string containing the results of
        the rss parser.
        :return: A string containing the json representation of the results
        """
        return self.feed.to_json()

    @property
    def feed(self):
        return Feed(self.feed_title, self.url, self.parsed_items)


class CacheReader:
    """
    This class represents the methods for caching rss data and retrieving already cached data.
    """

    def __init__(self, cache_path: str = 'rss_cache.bin'):
        self._cache_path = cache_path

    @property
    def cache(self) -> RSSCache:
        """
        This cache property retrieves the RSS feed data from a pickle file.
        :return: An instance of the RSSCache class.
        """
        with open(self._cache_path, 'rb') as cache:
            logging.info('Loading cached data.')
            return pickle.load(cache)

    @cache.setter
    def cache(self, obj: RSSCache):
        """
        This cache setter is used to store the RSS feed data in a pickle file.
        :param obj:RSSCache: RSSCache object to be stored in the cache file.
        """
        with open(self._cache_path, 'wb') as cache:
            sys.setrecursionlimit(10000)
            pickle.dump(obj, cache)
            logging.info('Finished caching data.')

    @validate_method_args
    def cache_results(self, current_items: Feed):
        """
        This function will serialize passed results into a BIN file along with the existing cache.
        """
        existing_cache = None
        if os.path.exists(self._cache_path) and os.path.getsize(self._cache_path):
            existing_cache = self.cache
            existing_cache.append(current_items)
        else:
            current_items = RSSCache([current_items])
        self.cache = existing_cache if existing_cache else current_items
        logging.info(f'Parsing results were successfully cached to: {self._cache_path}')
