"""
Test module for Parser object
"""
import sys
import unittest
import argparse
from ..parsers import Parser


class ParserTest(unittest.TestCase):
    """
    Parser tests.
    """

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        sys.argv[1:] = []

    def test_parser_instances(self):
        """
        Tests instances of parser object and instances its values
        :return:
        """
        parser = Parser()
        self.assertIsInstance(parser, Parser)
        self.assertIsInstance(parser.parser, argparse.ArgumentParser)
        self.assertIsInstance(parser.args, argparse.Namespace)
        self.assertIsInstance(parser.args_as_dict(), dict)

    def test_parser_argument_existence(self):
        """
        Tests for existence (or not) of arguments in a self parser object
        :return:
        """
        parser = Parser()
        parser_args = parser.args_as_dict()
        self.assertIn("source", parser_args)
        self.assertIn("limit", parser_args)
        self.assertIn("json", parser_args)
        self.assertIn("verbose", parser_args)
        self.assertIn("version", parser_args)
        self.assertNotIn("to_pdf", parser_args)
        self.assertNotIn("to_html", parser_args)

    def test_parser_arguments_value(self):
        """
        Tests for values matching after test object initialization
        :return:
        """
        sys.argv.extend(
            ["https://www.buzzfeed.com/world.xml", "--limit", "3", "--json", "--to-html", "--to-pdf", "test"]
        )
        parser = Parser()
        parser_args = parser.args_as_dict()
        print()
        self.assertEqual(parser_args.get("source"), "https://www.buzzfeed.com/world.xml")
        self.assertEqual(parser_args.get("limit"), 3)
        self.assertTrue(parser_args.get("json"))
        self.assertFalse(parser_args.get("verbose"))
        self.assertFalse(parser_args.get("version"))
        self.assertTrue(parser_args.get("to_pdf"))
        self.assertFalse(parser_args.get("to_html"))  # `to_html` key has "" value by const value
        self.assertEqual(parser_args.get("to_pdf"), "test")
        self.assertEqual(parser_args.get("to_html"), "")
