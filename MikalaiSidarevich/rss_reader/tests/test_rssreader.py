"""Test RssReader class."""

from unittest import TestCase
from unittest.mock import patch

from engine.rssreader import RssReader


class TestRssReader(TestCase):
    """Testcase for RssReader class."""

    def setUp(self):
        """
        Prepare test fixture.
        """
        self.reader = RssReader(verbose=False)

    @patch('engine.rssparser.RssParser.feed')
    def test_read_rss(self, mock_parser_feed):
        """
        read_rss() test.
        """
        mock_parser_feed.return_value = [{'channel': "",
                                          'entries': [{'title': "",
                                                       'date': "",
                                                       'date_fmt': "",
                                                       'link': "",
                                                       'description': "",
                                                       'image_link': "",
                                                       'image_data': ""}]}]

        url = "https://news.yahoo.com/rss/"
        limit = 1
        date = None
        self.assertIsNotNone(self.reader.read_rss(url, limit, False, date))
        self.assertIsNotNone(self.reader.read_rss(url, limit, True, date))
