from abc import ABC, abstractmethod

from rss_parse.parse.rss_feed import RssFeed, RssItem
from rss_parse.parse.rss_feed_mapper import RSS_FEED_JSON_MAPPER
from rss_parse.utils.formatting_utils import format_date_pretty, get_description_plain
from rss_parse.utils.message_consumer import MESSAGE_CONSUMER_NOOP


class RssProcessor(ABC):

    def __init__(self, rss_feed, mc=MESSAGE_CONSUMER_NOOP):
        self.rss_feed = rss_feed
        self._mc = mc

    @abstractmethod
    def process(self):
        pass


class RssPrinter(RssProcessor):
    __SEPARATOR = "----------"

    def __init__(self, rss_feed: RssFeed, file_descriptor, mc=None):
        super().__init__(rss_feed, mc)
        self.file_descriptor = file_descriptor

    def process(self):
        self._mc.add_message("Staring to print the feed in a human-readable format")
        self.__print()
        self.print_items_info()
        self._mc.add_message("Finishing printing")

    def print_items_info(self):
        rss_items = self.rss_feed.rss_items
        for item in rss_items:
            self.print_item_info(item)
            self.__print()
            self.__print(RssPrinter.__SEPARATOR)
            self.__print()

    def print_item_info(self, item: RssItem):
        self.__print(f"Title: {item.title}")
        self.__print(f"Date: {format_date_pretty(item.publication_date)}")
        self.__print(f"Link: {item.link}")

        image_url = item.image_url
        if image_url:
            image_title = item.title
            self.__print(f"Image: [{image_title}]({image_url})]")

        if item.description:
            self.__print()
            self.__print(get_description_plain(item.description))

    def __print(self, v="", sep=None):
        print(v, file=self.file_descriptor, sep=sep)


class RssJsonPrinter(RssProcessor):

    def process(self):
        self._mc.add_message("Converting to json")

        json_str = RSS_FEED_JSON_MAPPER.to_json(self.rss_feed, indent=4, pretty=True)

        self._mc.add_message("Printing json")
        print(json_str)
        self._mc.add_message("Printing finished")
