"""
Module for CacheWorker class

exports CacheWorker class
"""
import os
import utils.config as config
from appdirs import user_cache_dir
from datetime import datetime
from json import dumps, load
from feed import Feed
from utils.exceptions import CachedFeedNotFoundError


class CacheWorker:
    """Class for working with feeds caching"""

    appname = config.appname
    appauthor = config.appauthor

    @staticmethod
    def store_feed_in_cache(feed: Feed):
        """
        Function that stores feed in cache files

        Args:
            feed:   Feed object with all necessary data
        """

        date = str(datetime.strptime(feed.date, "%a, %d %b %Y %H:%M:%S %z").date())
        source = feed.source_url
        feed_id = feed.link
        config.verbose_print("Getting user cache directory", "bold")
        cache_dir = user_cache_dir(CacheWorker.appname, CacheWorker.appauthor)
        if not os.path.exists(cache_dir):
            os.mkdir(cache_dir)
        config.verbose_print("Checking user cache directory overload", "und")
        cache_files = []
        for (_, __, filenames) in os.walk(cache_dir):
            for file in filenames:
                if file.endswith(".json"):
                    cache_files.append(file)
        if len(cache_files) > 10:
            config.verbose_print("User cache directory is overloaded. Removing old cache file", "warn")
            os.remove(os.path.join(cache_dir, f"{cache_files[0]}"))
        try:
            with open(os.path.join(cache_dir, f"{date}.json"), "r") as cache_file:
                config.verbose_print("Reading date cache file", "bold")
                try:
                    cache = load(cache_file)
                except Exception as e:
                    config.verbose_print(f"Warning: JSON not found ({e})", "warn")
                    cache = dict()
        except Exception as e:
            config.verbose_print(f"Warning: date cache not found ({e})", "warn")
            cache = dict()
        config.verbose_print("Checking date cache file overload", "und")
        if len(cache.keys()) > 10:
            config.verbose_print("Date cache file is overloaded. Removing old cache entry", "warn")
            del cache[list(cache.keys())[0]]
        try:
            with open(os.path.join(cache_dir, f"{date}.json"), "w") as cache_file:
                config.verbose_print("Checking if feed is already in cache", "und")
                feed_is_in_cache = False
                if source in cache:
                    for feed in cache[source]:
                        if feed_id in feed:
                            config.verbose_print("Feed is in cache already", "green")
                            feed_is_in_cache = True
                            break
                    if not feed_is_in_cache:
                        config.verbose_print("Feed not in cache. Storing feed in cache", "bold")
                        if len(cache[source]) > 10:
                            cache[source].pop(0)
                        cache[source].append(feed.to_json())
                else:
                    cache[source] = [feed.to_json()]
                config.verbose_print("Update date cache file", "bold")
                cache_file.write(dumps(cache, indent=4))
        except Exception as e:
            config.verbose_print(f"Unable to open cache file ({e})", "warn")

    @staticmethod
    def read_feed_from_cache(date: str, source: str or None, limit: int or None) -> [Feed]:
        """
        Args:
            date:   for which date cached feed should be read
            source: specific source for feed
            limit:  limit of feeds that should be retrieved

        Returns:
            [Feed]: list of fetched feeds from cache

        Raises:
            CachedFeedNotFoundError
        """

        config.verbose_print("Opening user cache directory", "bold")
        cache_dir = user_cache_dir(CacheWorker.appname, CacheWorker.appauthor)
        try:
            with open(os.path.join(cache_dir, f"{date}.json"), "r") as cache_file:
                try:
                    cache = load(cache_file)
                except Exception as e:
                    config.verbose_print(f"Cannot read JSON from cache file ({e})", "warn")
                    cache = dict()
                if len(cache.keys()) == 0:
                    raise CachedFeedNotFoundError("Error: Cached Feed not found")
                formatted_cached_feeds = []
                limit_final = 100
                if limit is not None:
                    limit_final = limit
                config.verbose_print("Reading feeds from cache", "bold")
                if source is None:
                    for cached_feed in cache.values():
                        if len(formatted_cached_feeds) == limit_final:
                            break
                        formatted_cached_feeds.append(Feed.json_to_feed(cached_feed[0]))
                else:
                    for cached_feed in cache[source]:
                        if len(formatted_cached_feeds) == limit_final:
                            break
                        formatted_cached_feeds.append(Feed.json_to_feed(cached_feed))
                return formatted_cached_feeds
        except Exception as e:
            config.verbose_print(f"Date cache file not found ({e})", "warn")
            raise CachedFeedNotFoundError("Error: Cached Feed not found")
