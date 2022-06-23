from django.db import models
from urllib.parse import urlparse


class Cache(models.Model):
    url = models.TextField(max_length=200, verbose_name="RSS feed", unique=True)
    cache = models.JSONField(blank=True, null=True, verbose_name="Cached news")

    class Meta:
        verbose_name = 'RSS feed'
        verbose_name_plural = 'RSS feeds'

    def __str__(self):
        feed_name = urlparse(self.url).netloc.split('.')[-2].capitalize()
        return feed_name
