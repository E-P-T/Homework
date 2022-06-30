import unittest
from argparse import ArgumentTypeError
from rss_reader_package.date import valid_date


class TestDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(str(valid_date("20210730")), "2021-07-30")
        with self.assertRaises(ArgumentTypeError):
            valid_date("word")
        with self.assertRaises(ArgumentTypeError):
            valid_date(valid_date("30071999"))


unittest.main()
