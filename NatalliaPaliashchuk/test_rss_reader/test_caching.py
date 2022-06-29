import unittest
import os
from rss_reader.caching import *
from .test_feed import test_feed
from rss_reader.exceptions import CachingError


class TestCaching(unittest.TestCase):
    def test_caching(self, *args):
        cache_feed({'url': test_feed})
        cached_feed = get_feed_by_date(test_feed['feed_items'][0]['item_pub_date'], 'url', 1)
        self.assertEqual(cached_feed['url'], test_feed)
        none_cached_feed = get_feed_by_date(test_feed['feed_items'][0]['item_pub_date'], 'not_url', 1)
        self.assertIsNone(none_cached_feed)
        os.remove('cache.pk1')
        self.assertRaises(CachingError, get_feed_by_date, test_feed['feed_items'][0]['item_pub_date'], 'url', 1)


if __name__ == '__main__':
    unittest.main()
