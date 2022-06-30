import unittest

from reader import Reader
from converter import Converter
from printer import Printer


class TestReader(unittest.TestCase):

    def setUp(self):
        self.reader1 = Reader("https://www.onliner.by/feed", 1)
        self.reader2 = Reader("https://www.onliner.by/feed", 2)

    def test_get_acces(self):
        self.assertEqual(type(self.reader1.get_title()), list)

    def test_get_title(self):
        self.assertEqual(len(self.reader1.get_title()), 1)

    def test_get_pubDate(self):
        self.assertEqual(len(self.reader2.get_pubDate()), 2)

    def test_get_link(self):
        self.assertEqual(len(self.reader2.get_pubDate()), 2)

    def test_get_descriprion(self):
        self.assertEqual(len(self.reader1.get_pubDate()), 1)

    def test_get_acces(self):
        self.assertEqual(type(self.reader1.get_title()), list)


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter1 = Converter(Reader("https://feeds.fireside.fm/bibleinayear/rss", 3))
        self.converter2 = Converter()

    def test_to_dict(self):
        self.assertEqual(len(self.converter1.to_dict()), 6)

    def test_from_json(self):
        self.assertEqual(len(self.converter1.from_json()), 6)

    def test_from_json2(self):
        self.assertEqual(type(self.converter2.from_json()), dict)

    def test_to_HTML(self):
        self.assertEqual(self.converter1.to_HTML(), True)


class TestPrinter(unittest.TestCase):
    def setUp(self):
        self.converter1 = Converter(Reader("https://feeds.fireside.fm/bibleinayear/rss", 3))
        self.printer = Printer(self.converter1.from_json())

    def test_print(self):
        print(self.printer)


if __name__ == "__main__":
    unittest.main()

