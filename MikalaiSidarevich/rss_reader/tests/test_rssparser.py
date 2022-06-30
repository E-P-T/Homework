"""Test RssParser class."""

from unittest import TestCase

from engine.rsscacher import RssCacher
from engine.rssparser import RequestError, RssParser


class TestRssParser(TestCase):
    """Testcase for RssParser class."""

    def test_feed(self):
        """
        feed() test.
        """
        with RssCacher(":memory:", verbose=False) as db:
            self.parser = RssParser(db, verbose=False)

            with self.assertRaises(RequestError):
                self.parser.feed("", 1)

            self.assertIsNotNone(self.parser.feed("https://news.yahoo.com/rss/", 1))
