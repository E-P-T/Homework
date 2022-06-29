from abc import ABC, abstractmethod

from rss_parse.exceptions.exceptions import CacheException
from rss_parse.parse.rss_cache import TmpDirectoryCache
from rss_parse.parse.rss_feed import RssFeed
from rss_parse.utils.messaging_utils import MESSAGE_CONSUMER_NOOP


class RssPreprocessor(ABC):
    """
    Abstraction to do preprocess/modify RSS Feed
    """

    def __init__(self, mc=MESSAGE_CONSUMER_NOOP):
        self._mc = mc

    @abstractmethod
    def preprocess(self, rss_feed: RssFeed) -> RssFeed:
        """
        Method gets RSS Feed as an input and returns modified view of it
        """
        pass


class RssCachePreprocessor(RssPreprocessor):
    """
    Implementation of RSSPreprocessor that stores RSS Feed in cache
    """

    def preprocess(self, rss_feed):
        self._mc.add_message("Trying to add fetched news to the local cache")
        try:
            rss_cache = TmpDirectoryCache(rss_feed, mc=self._mc)
            rss_cache.cache()
        except CacheException:
            self._mc.add_message("Unable to save RSS Feed to cache. Proceeding...")
        return rss_feed


class RssSortPreprocessor(RssPreprocessor):
    """
    Implementation of RSSPreprocessor that sorts RSS Feed by publication date descending
    """

    def preprocess(self, rss_feed):
        rss_items = sorted(rss_feed.rss_items, key=lambda item: item.publication_date, reverse=True)
        return RssFeed(rss_items)


class RssLimitPreprocessor(RssPreprocessor):
    """
    Implementation of RSSPreprocessor that gets limited number of  RSS Items from RSS Feed
    """

    def __init__(self, limit, mc=None):
        super().__init__(mc)
        self.__limit = limit

    def preprocess(self, rss_feed):
        rss_items = rss_feed.rss_items[:self.__limit]
        return RssFeed(rss_items)
