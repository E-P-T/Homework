from django.db import IntegrityError

from reader.models import Cache
from rss_reader import rss_reader


class DjangoRssReader(rss_reader.RssReader):

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
            print('No news got for caching')


class DjangoRssReaderCached(rss_reader.RssReaderCached):
    @staticmethod
    def limit_news_dict(news_cache: dict, limit=None, news_url: str = '') -> dict:
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
            temp_news_dict = {'feed_title': f'Cached news',
                              'feed_description': f'Best news gathered for you and cached by our service',
                              'feed_link': f'News sources can be reached through links listed in news',
                              'feed_items': {},
                              }
        for url, feed in news_cache.items():
            for key, value in feed.items():
                if key == 'feed_items':
                    for news_tag, tag_text in value.items():
                        temp_news_dict['feed_items'][news_tag] = tag_text
        if len(temp_news_dict['feed_items']) == 0:
            raise rss_reader.rss_exceptions.NoDataInCache('No news found in cache')
        news_dict = rss_reader.RssReader.limit_news_dict(temp_news_dict, limit)
        return news_dict

