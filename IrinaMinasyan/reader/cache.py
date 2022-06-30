"""This class implements news items cache"""
import shelve

from dateutil.parser import parse
from reader.exceptions import CacheNotFound


class Cache:
    """Class which definite characteristics of the caching.
    Attributes
    cache : dict
        The format of the cached data that will be stored in the file.
        Cache format is {date: {url: set(news_article)}}.
    """
    def __init__(self):
        """Initialise empty cache"""
        self.cache = shelve.open('cache_rss')

    def save_in_cache(self, news, url):
        """Save news_articles to cache"""
        parsed_date = parse(news.get_date())
        date = parsed_date.strftime('%Y%m%d')
        key = date + url
        if key in self.cache:
            self.cache[key] += [[news, news.get_news()]]
        else:
            self.cache[key] = [[news, news.get_news()]]
        self.cache.close()

    def read_from_cache(self, date, url=None, limit=None):
        """Get cache for this url from file․ If the address
        is not specified receive all the news for that date,
        else receive news only for these urls and dates.
        """
        if not url:
            try:
                for key in self.cache.keys():
                    if key[:8] == date:
                        special_key = key
                return self.cache[special_key][:limit]
            except Exception:
                raise CacheNotFound
        else:
            key = date + url
            if key in self.cache:
                return self.cache[key][:limit]
            else:
                raise CacheNotFound
