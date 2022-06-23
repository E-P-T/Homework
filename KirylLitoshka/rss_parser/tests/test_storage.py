"""
Test module for Storage object
"""

import unittest
import os
import sys
import pathlib
from datetime import date

from ..storage import Storage, StorageError
from ..parsers import Parser
from ..rss import rss

TEST_LOCAL_STORAGE_NAME = "local"
TEST_STORAGE_DIR = os.path.join(pathlib.Path(__file__).parent, TEST_LOCAL_STORAGE_NAME)


class StorageTest(unittest.TestCase):
    """
    Storage Tests. Test storage object is created in class method
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.storage = Storage(TEST_STORAGE_DIR, TEST_LOCAL_STORAGE_NAME)
        cls.extensions = [".bak", ".dat", ".dir"]
        cls.parser = Parser()

    def setUp(self) -> None:
        for extension in self.extensions:
            file = self.storage.filepath + extension
            if os.path.exists(file):
                os.remove(file)

    def test_path_existence(self):
        """
        Checks path to directory of storage and after save some data, checking for existence of storage files
        :return:
        """
        self.assertTrue(os.path.exists(self.storage.path))
        self.storage.save("some key", [])
        for extension in self.extensions:
            self.assertTrue(os.path.exists(self.storage.filepath + extension))

    def test_empty_load(self):
        """
        Checks if data is empty after loading
        (because all data is deleted after each test)
        :return:
        """
        data = self.storage.load()
        self.assertIsInstance(data, dict)
        self.assertDictEqual(data, {})

    def test_load_after_parse(self):
        """
        Checks for loading data after successful parsing
        :return:
        """
        link = "https://auto.onliner.by/feed"
        sys.argv[1:] = [link, "--limit", "2"]
        parsed_data = self.parser.start_parse()
        self.storage.save(link, parsed_data.items)
        loaded_data = self.storage.load()
        self.assertIsInstance(loaded_data, dict)
        self.assertTrue(link in loaded_data)
        self.assertIsInstance(loaded_data[link], list)
        self.assertEqual(len(loaded_data[link]), 2)

    def test_load_by_date(self):
        """
        Checks for loading data by date
        :return:
        """
        link = "https://auto.onliner.by/feed"
        sys.argv[1:] = [link]
        parser_data = self.parser.start_parse()
        self.storage.save(link, parser_data.items)
        str_date = "".join(str(date.today()).split("-"))
        loaded_data = self.storage.load_by_date(str_date)
        self.assertIsInstance(loaded_data, list)
        self.assertTrue(len(loaded_data) > 0)
        self.assertIsInstance(loaded_data[0], rss.RssFeedItem)

    def test_load_by_date_with_exception(self):
        """
        Checks for an exception if saved data doesn't contain rss item with inputted date
        :return:
        """
        link = "https://auto.onliner.by/feed"
        sys.argv[1:] = [link]
        parser_data = self.parser.start_parse()
        self.storage.save(link, parser_data.items)
        with self.assertRaises(StorageError) as exc:
            loaded_data = self.storage.load_by_date("20220618")
            self.assertFalse(loaded_data)
        self.assertEqual("Data not found", exc.exception.args[0])
