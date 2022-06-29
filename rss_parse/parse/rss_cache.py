import os
import tempfile

from rss_parse.exceptions.exceptions import CacheException, ParsingException
from rss_parse.parse.rss_feed import RssFeed
from rss_parse.parse.rss_mapper import RSS_FEED_JSON_MAPPER
from rss_parse.parse.rss_parser import RssJsonParser
from rss_parse.utils.collection_utils import group_by, merge_by_key
from rss_parse.utils.messaging_utils import MESSAGE_CONSUMER_NOOP


class TmpDirectoryCache:
    """
    Class to store RSS Feed in a temporary directory
    """
    __DATE_TO_FILE_NAME_PATTERN = '%Y%m%d'

    def __init__(self, rss_feed, mc=MESSAGE_CONSUMER_NOOP):
        self.__rss_feed = rss_feed
        self.__mc = mc
        self.__base_dir = TmpDirectoryCache.get_cache_base_path()

    @staticmethod
    def get_cache_base_path():
        """
        Returns the directory where all Cached files are stored
        """
        return os.path.join(tempfile.gettempdir(), "rss_reader")

    @staticmethod
    def get_cache_path(pub_date):
        """
        Builds the path to the cache file based on a publication date
        """
        return os.path.join(TmpDirectoryCache.get_cache_base_path(),
                            f"{pub_date.strftime(TmpDirectoryCache.__DATE_TO_FILE_NAME_PATTERN)}.json")

    def cache(self):
        try:
            if not os.path.exists(self.__base_dir):
                os.mkdir(self.__base_dir)
        except:
            raise CacheException("Unable to create a directory for local cache")

        if not self.__rss_feed or not self.__rss_feed.rss_items:
            return

        feed_by_date = group_by(self.__rss_feed.rss_items,
                                key=lambda x: x.publication_date.strftime(
                                    TmpDirectoryCache.__DATE_TO_FILE_NAME_PATTERN))
        for pub_date, new_items in feed_by_date:
            file_name = os.path.join(self.__base_dir, f"{pub_date}.json")
            json_parser = RssJsonParser(file_name, self.__mc)
            existing_items = json_parser.parse().rss_items
            all_items = merge_by_key([*existing_items, *new_items], key=lambda x: x.key())
            all_feed = RssFeed(all_items)
            rss_json = RSS_FEED_JSON_MAPPER.to_json(all_feed)
            with open(file_name, "w", encoding="UTF-8") as f:
                f.write(rss_json)


class CacheJsonParser(RssJsonParser):
    """
    Class to read RSS Feed from a cached directory
    """

    def __init__(self, date, source, mc=None):
        super().__init__(TmpDirectoryCache.get_cache_path(date), mc)

        self.__source = source

    def parse(self):
        """
        Class to read RSS Feed from a cached directory.
        Raises an exception if no news for the date found.
        """
        rss_feed = super().parse()
        items = rss_feed.rss_items
        if self.__source:
            items = [item for item in items if item.source == self.__source]
        if not items:
            raise ParsingException("No cached news for the date")
        return RssFeed(items)
