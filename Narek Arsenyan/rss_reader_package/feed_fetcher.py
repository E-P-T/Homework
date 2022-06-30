"""
Module for FeedFetcher class

exports FeedFetcher class
"""
import requests
from bs4 import BeautifulSoup
import utils.config as config
from link import Link
from feed import Feed
from cache_worker import CacheWorker
from utils.exceptions import WrongLimitError, WrongUrlError


class FeedFetcher:
    """Class for fetching feeds and storing feeds"""

    def __init__(self, source: str, limit: int or None):
        """
        The constructor for FeedFetcher class

        Args:
            source: the source url of rss feeds
            limit:  limit of the feeds, that must be shown

        Raises:
            WrongLimitError
        """

        if limit is not None and limit < 1:
            raise WrongLimitError("Argument LIMIT must be greater than 0")

        self.__source = source
        self.__limit = limit
        self.feeds_formatted = []

    def fetch_feeds(self):
        """The function that fetches and stores feeds using source and limit of object """

        try:
            r = requests.get(self.__source)
            soup = BeautifulSoup(r.content, features="xml")
            source_title = soup.find("channel").find("title").text
            config.verbose_print("Feeds fetched", "green")
            if self.__limit is None:
                limit = 100
            else:
                limit = self.__limit
            items = soup.find_all('item')[:limit]
            for item in items:
                config.verbose_print("Scraping feed title", "bold")
                title = item.find('title').text
                config.verbose_print("Scraping publish date", "bold")
                date = item.find('pubDate').text
                config.verbose_print("Scraping feed link", "bold")
                link = item.find('link').text
                config.verbose_print("Scraping feed content", "bold")
                raw_content = item.find('description').text
                config.verbose_print("Scraping media links", "bold")
                media_links_raw = item.find_all("enclosure")
                config.verbose_print("Scraping non-media links", "bold")
                content = BeautifulSoup(raw_content, 'lxml')
                feed_links_raw = content.find_all("a", href=True)
                media_links = list()
                feed_links = list()
                for feed_link in feed_links_raw:
                    feed_links.append(Link(feed_link['href'], 'link'))
                for media_link in media_links_raw:
                    media_links.append(Link(media_link["url"], media_link["type"].split("/")[0]))
                config.verbose_print("Storing fetched feeds in cache", "bold")
                formatted_feed = Feed(source_title, self.__source, title, date, link, raw_content, feed_links, media_links)
                CacheWorker.store_feed_in_cache(formatted_feed)
                self.feeds_formatted.append(formatted_feed)
        except Exception:
            raise WrongUrlError("Specified url is not rss type")
