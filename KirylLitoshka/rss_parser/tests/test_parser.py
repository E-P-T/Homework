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
        sys.argv.extend(["https://www.buzzfeed.com/world.xml", "--limit", "3", "--json"])
        self.parser = Parser()
        self.args = self.parser.args_as_dict()

    def tearDown(self) -> None:
        sys.argv[1:] = []

    def test_parser_instances(self):
        """
        Tests instances of parser object and instances its values
        :return:
        """
        self.assertIsInstance(self.parser, Parser)
        self.assertIsInstance(self.parser.parser, argparse.ArgumentParser)
        self.assertIsInstance(self.parser.args, argparse.Namespace)
        self.assertIsInstance(self.parser.args_as_dict(), dict)

    def test_parser_argument_existence(self):
        """
        Tests for existence of arguments in a self parser object
        :return:
        """
        self.assertIn("source", self.args)
        self.assertIn("limit", self.args)
        self.assertIn("json", self.args)
        self.assertIn("verbose", self.args)
        self.assertIn("version", self.args)

    def test_parser_arguments_value(self):
        """
        Tests for values matching after test object initialization
        :return:
        """
        self.assertEqual(self.args.get("source"), "https://www.buzzfeed.com/world.xml")
        self.assertEqual(self.args.get("limit"), 3)
        self.assertTrue(self.args.get("json"))
        self.assertFalse(self.args.get("verbose"))
        self.assertFalse(self.args.get("version"))
