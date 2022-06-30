import unittest
from rss_reader_package.feed_fetcher import FeedFetcher
from rss_reader_package.utils.exceptions import WrongLimitError, WrongUrlError


class TestFeedFetcher(unittest.TestCase):
    def test_feed_fetcher(self):
        with self.assertRaises(WrongLimitError):
            FeedFetcher("source", -1)
        with self.assertRaises(WrongUrlError):
            ff = FeedFetcher("source", None)
            ff.fetch_feeds()
        ff2 = FeedFetcher("https://timesofindia.indiatimes.com/rssfeedstopstories.cms", 1)
        ff2.fetch_feeds()
        self.assertEqual(len(ff2.feeds_formatted), 1)
        ff3 = FeedFetcher("https://timesofindia.indiatimes.com/rssfeedstopstories.cms", 3)
        ff3.fetch_feeds()
        self.assertEqual(len(ff3.feeds_formatted), 3)


unittest.main()
