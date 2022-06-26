from django.db import IntegrityError

from reader.models import Cache
from rss_reader import rss_reader


class DjangoRssReader(rss_reader.RssReader):

    def __init__(self, url: str, news_limit: int = None):
        """
        Method serves for processing news from rss feeds
        On object creation it gathers required news data, updates news cache and processes data for future output
        :param url: URL of rss-feed
        """
        self.url = url
        self.news_cache = rss_reader.RssReader.prepare_dict(url)
        if self.news_cache:  # to prevent further funcs if prepare_dict failed
            rss_reader.RssReader.update_local_cache(self.url, self.news_cache)
            self.news_dict = rss_reader.RssReader.limit_news_dict(self.news_cache, news_limit)

    def save_django_reader_cache(self):
        cache_dict = {"url": self.url, 'cache': self.news_cache}
        if cache_dict['cache']:
            c = Cache(**cache_dict)
            try:
                c.save()
            except IntegrityError:
                cache = Cache.objects.filter(url=self.url).first()
                cache.cache = c.cache
                cache.save()
        else:
            raise ValueError('No news found in URL, please check URL')


class DjangoRssReaderCached(rss_reader.RssReaderCached):
    @staticmethod
    def limit_news_dict(news_cache: dict, limit=None, news_url: str = '', news_date: str = '') -> dict:
        """
        """
        if news_url and rss_reader.RssReaderCached.validate_url(news_url):
            rss_reader.RssReader.log_runtime(f'Choosing news according to set url: {news_url}')
            news_cache = {url: feed for url, feed in news_cache.items() if url == news_url}
            if len(news_cache) == 0:
                raise rss_reader.rss_exceptions.NoDataInCache('No news from such URL in cache or not a valid rss URL')
        if news_url:
            temp_news_dict = {key: value for url in news_cache.values() for key, value in url.items()
                              if key != 'feed_items'}
            temp_news_dict['feed_items'] = {}
        else:
            temp_news_dict = {'feed_title': f'Cached news of {news_date if news_date else "recent time"}',
                              'feed_description': f'Best news gathered for you and cached by our service',
                              'feed_link': f'News sources can be reached through links listed in news',
                              'feed_items': {},
                              }
        for url, feed in news_cache.items():
            for key, value in feed.items():
                if key == 'feed_items':
                    for news_tag, tag_text in value.items():
                        if news_date:
                            if news_date in news_tag:
                                temp_news_dict['feed_items'][news_tag] = tag_text
                        else:
                            temp_news_dict['feed_items'][news_tag] = tag_text
        if len(temp_news_dict['feed_items']) == 0:
            raise rss_reader.rss_exceptions.NoDataInCache('No news found in cache')
        news_dict = rss_reader.RssReader.limit_news_dict(temp_news_dict, limit)
        return news_dict

