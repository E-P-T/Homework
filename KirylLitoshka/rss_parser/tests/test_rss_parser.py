"""
Test module for RSS parser object
"""

import unittest
import warnings
import sys
import json
from requests.exceptions import ConnectionError as ConnError
from ..rss import RssFeed
from ..parsers import Parser, RssParser


class RSSParserTest(unittest.TestCase):
    """
    RSS Parser Tests. Each new test will run with new Parser object (for args difference)
    """

    @classmethod
    def setUpClass(cls) -> None:
        warnings.filterwarnings("ignore", module="bs4")

    def setUp(self) -> None:
        self.parser = Parser()

    def tearDown(self) -> None:
        sys.argv[1:] = []

    def test_output_rss_data(self):
        """
        Based result existence checks and result instance checks
        :return:
        """
        sys.argv[1:] = ["https://auto.onliner.by/feed", "--limit", "2"]
        data = Parser().start_parse()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, RssFeed)

    def test_output_rss_into_json(self):
        """
        Checks parsing with --json argument
        :return:
        """
        sys.argv[1:] = ["https://auto.onliner.by/feed", "--limit", "2"]
        data = json.loads(Parser().start_parse().to_json())
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data["items"]), 2)
        self.assertIsInstance(data["items"], list)

    def test_output_with_version_flag(self):
        """
        Checks parsing with --version argument
        :return:
        """
        sys.argv.extend(["https://www.buzzfeed.com/world.xml", "--limit", "3", "--version"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        self.assertEqual(rss.get_data(), 1.4)

    def test_exception_with_negative_limit(self):
        """
        Checks for an exception if inputted limit less or equal zero
        :return:
        """
        sys.argv.extend(["https://www.buzzfeed.com/world.xml", "--limit", "-2", "--json"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        with self.assertRaises(Exception) as exc:
            rss.get_data()
        self.assertEqual("Limit must be more that zero", exc.exception.args[0])

    def test_exception_with_empty_source(self):
        """
        Checks for an exception if inputted arguments haven't a source argument
        :return:
        """
        sys.argv.extend(["--limit", "7", "--json"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        with self.assertRaises(Exception) as exc:
            rss.get_data()
        self.assertEqual("URL cannot be empty", exc.exception.args[0])

    def test_connection_error(self):
        """
        Checks for an exception if inputted source (url) is incorrect
        or something went wrong with internet connection
        :return:
        """
        sys.argv.extend(["https://www.bu.com/world.xml", "--limit", "3", "--json"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        with self.assertRaises(ConnError) as exc:
            rss.get_data()
        self.assertEqual(f"Failed Connect to {args.get('source')}", exc.exception.args[0])

    def test_invalid_url(self):
        """
        Simple checks for and exception if url name not starts with http
        :return:
        """
        sys.argv.extend(["www.bu.com/world.xml"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        with self.assertRaises(Exception) as exc:
            rss.get_data()
        self.assertEqual("Fail! Invalid URL", exc.exception.args[0])

    def test_non_rss_url(self):
        """
        Checks for an exception if url is valid, but it's not a rss feed
        :return:
        """
        sys.argv.extend(["https://onliner.by"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        with self.assertRaises(Exception) as exc:
            rss.get_data()
        self.assertEqual("URL is not an RSS feed", exc.exception.args[0])
