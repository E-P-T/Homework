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
    pass

