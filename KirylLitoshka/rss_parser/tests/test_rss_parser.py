import json
import sys
import unittest
import argparse
import warnings
from rss_parser.parsers import Parser, RssParser
from rss_parser.rss import RssFeed


class ParserTest(unittest.TestCase):
    def setUp(self) -> None:
        sys.argv.extend(["https://www.buzzfeed.com/world.xml", "--limit", "3", "--json"])
        self.parser = Parser()
        self.args = self.parser.args_as_dict()

    def tearDown(self) -> None:
        sys.argv[1:] = []

    def test_parser_instances(self):
        self.assertIsInstance(self.parser, Parser)
        self.assertIsInstance(self.parser.parser, argparse.ArgumentParser)
        self.assertIsInstance(self.parser.args, argparse.Namespace)
        self.assertIsInstance(self.parser.args_as_dict(), dict)

    def test_parser_argument_existence(self):
        self.assertIn("source", self.args)
        self.assertIn("limit", self.args)
        self.assertIn("json", self.args)
        self.assertIn("verbose", self.args)
        self.assertIn("version", self.args)

    def test_parser_arguments_value(self):
        self.assertEqual(self.args.get("source"), "https://www.buzzfeed.com/world.xml")
        self.assertEqual(self.args.get("limit"), 3)
        self.assertTrue(self.args.get("json"))
        self.assertFalse(self.args.get("verbose"))
        self.assertFalse(self.args.get("version"))


class RSSParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        warnings.filterwarnings("ignore", module="bs4")

    def setUp(self) -> None:
        self.parser = Parser()

    def tearDown(self) -> None:
        sys.argv[1:] = []

    def test_output_rss_data(self):
        sys.argv[1:] = ["https://auto.onliner.by/feed", "--limit", "2"]
        data = Parser().start_parse()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, RssFeed)

    def test_output_rss_into_json(self):
        sys.argv[1:] = ["https://auto.onliner.by/feed", "--limit", "2"]
        data = json.loads(Parser().start_parse().to_json())
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data["items"]), 2)
        self.assertIsInstance(data["items"], list)

    def test_output_with_version_flag(self):
        sys.argv.extend(["https://www.buzzfeed.com/world.xml", "--limit", "3", "--version"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        self.assertEqual(rss.get_data(), 1.0)

    def test_exception_with_negative_limit(self):
        sys.argv.extend(["https://www.buzzfeed.com/world.xml", "--limit", "-2", "--json"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        with self.assertRaises(Exception) as e:
            rss.get_data()
        self.assertEqual("Limit must be more that zero", e.exception.args[0])

    def test_exception_with_empty_source(self):
        sys.argv.extend(["--limit", "7", "--json"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        with self.assertRaises(Exception) as e:
            rss.get_data()
        self.assertEqual("URL cannot be empty", e.exception.args[0])

    def test_connection_error(self):
        sys.argv.extend(["https://www.bu.com/world.xml", "--limit", "3", "--json"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        with self.assertRaises(Exception) as e:
            rss.get_data()
        self.assertEqual(f"Failed Connect to {args.get('source')}", e.exception.args[0])

    def test_invalid_url(self):
        sys.argv.extend(["www.bu.com/world.xml"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        with self.assertRaises(Exception) as e:
            rss.get_data()
        self.assertEqual("Fail! Invalid URL", e.exception.args[0])

    def test_non_rss_url(self):
        sys.argv.extend(["https://onliner.by"])
        args = self.parser.args_as_dict()
        rss = RssParser(**args)
        with self.assertRaises(Exception) as e:
            rss.get_data()
        self.assertEqual("URL is not an RSS feed", e.exception.args[0])


if __name__ == "__main__":
    unittest.main()
