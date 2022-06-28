import xml
from abc import ABC, abstractmethod

import requests
import xmltodict
from requests.exceptions import InvalidSchema, InvalidURL, MissingSchema

from rss_parse.exceptions.exceptions import ParsingException
from rss_parse.parse.rss_feed import RssFeed, RssItem
from rss_parse.parse.rss_keys import *
from rss_parse.utils.message_consumer import MESSAGE_CONSUMER_NOOP
from rss_parse.utils.parsing_utils import sanitize_text, to_date


class RssParser(ABC):

    def __init__(self, mc=MESSAGE_CONSUMER_NOOP):
        self._mc = mc

    @abstractmethod
    def parse(self):
        """
        :rtype: rss_parse.rss_feed.RssFeed
        """
        pass


class RssXmlParser(RssParser):

    def __init__(self, xml_feed, mc=None):
        super().__init__(mc)
        self.__xml_feed = xml_feed
        self._mc = mc

    def parse(self):

        self._mc.add_message("Parsing RSS Feed by elements")
        try:
            rss_feed_dict = xmltodict.parse(self.__xml_feed)[RSS_ROOT]
        except (xml.parsers.expat.ExpatError, KeyError):
            # TODO: include original exception to the
            raise ParsingException("Source doesn't contain a valid RSS Feed.")

        self._mc.add_message("Parsing items info")
        rss_items = self.parse_items(rss_feed_dict)

        self._mc.add_message("Parsing finished")
        return RssFeed(rss_items)

    def parse_items(self, rss_feed_dict):
        rss_items_raw = rss_feed_dict[RSS_CHANNEL][RSS_ITEMS]
        res = []
        for rss_item_dict in rss_items_raw:
            item = self.parse_item(rss_item_dict)
            if self.__validate_correctness(item):
                res.append(item)
            else:
                self._mc.add_message("Item skipped because it is invalid (required fields are absent)")
        return res

    def parse_item(self, rss_item_dict):
        title = sanitize_text(rss_item_dict.get(RSS_ITEM_TITLE, None))
        description = rss_item_dict.get(RSS_ITEM_DESCRIPTION, None)
        publication_date = to_date(rss_item_dict.get(RSS_ITEM_PUB_DATE, None))
        link = rss_item_dict.get(RSS_ITEM_LINK, None)
        image_url = self.parse_image(rss_item_dict)

        return RssItem(title, description, publication_date, link, image_url)

    def parse_image(self, rss_item_dict):
        image_url = rss_item_dict.get(RSS_IMAGE_ROOT, None)
        if not image_url:
            image_url = rss_item_dict.get(RSS_IMAGE_ROOT_MEDIA_CONTENT, {}).get(RSS_IMAGE_URL_ATTR, None)
        if not image_url:
            image_url = rss_item_dict.get(RSS_IMAGE_ROOT_MEDIA_THUMBNAIL, {}).get(RSS_IMAGE_URL_ATTR, None)
        if not image_url:
            enclosure = rss_item_dict.get(RSS_IMAGE_ROOT_ENCLOSURE, {})
            if enclosure.get('@type', "").startswith("image/"):
                image_url = enclosure.get(RSS_IMAGE_URL_ATTR, None)
        return image_url

    def __validate_correctness(self, item: RssItem):
        return item.title and item.publication_date and item.link


class RssUrlParser(RssParser):

    def __init__(self, source, mc=None):
        # FIXME: assert source is not None, "Source URL is required"
        super().__init__(mc)
        self.__source = source
        self._mc = mc

    def parse(self):
        try:
            self._mc.add_message(f"Reaching out to {self.__source}")
            with requests.get(self.__source) as f:
                # TODO: add error handling
                rss_raw_xml = f.text
        except (InvalidSchema, InvalidURL, MissingSchema):
            self._mc.add_message(f"Encountered an error during reading RSS Feed from URL")
            raise ParsingException(f"Invalid source URL: {self.__source}")
        except:  # ConnectionError
            self._mc.add_message(f"Unable to connect")
            raise ParsingException(f"Unable to connect to {self.__source}")

        rss_xml_parser = RssXmlParser(rss_raw_xml, mc=self._mc)

        feed = rss_xml_parser.parse()
        for item in feed.rss_items:
            item.source = self.__source

        return feed
