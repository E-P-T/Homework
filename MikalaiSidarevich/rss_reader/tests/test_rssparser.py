"""Test RssParser class."""

from unittest import TestCase

from engine.rssparser import RequestError, RssParser


class TestRssParser(TestCase):
    """Testcase for RssParser class."""

    def setUp(self):
        """
        Prepare test fixture.
        """
        self.parser = RssParser(verbose=False)

    def test_feed(self):
        """
        feed() test.
        """
        with self.assertRaises(RequestError):
            self.parser.feed("", 1)

        self.assertIsNotNone(self.parser.feed("https://news.yahoo.com/rss/", 1))
