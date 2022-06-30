import os
import shutil
import unittest
from rss_reader_package.format_converter import FormatConverter
from rss_reader_package.mocks.raw_feed_mock import mock_feed_raw
from rss_reader_package.feed import Feed
from appdirs import user_data_dir
from rss_reader_package.utils.count_files import count_files_by_type
from rss_reader_package.utils.exceptions import NotSupportedConversionFormat


class TestFormatConverter(unittest.TestCase):
    parsed_feed = Feed.json_to_feed(mock_feed_raw)

    def test_convert_feeds(self):
        user_dir = user_data_dir()
        with self.assertRaises(NotSupportedConversionFormat):
            FormatConverter.convert_feeds([TestFormatConverter.parsed_feed], "my_format", None, False)
        os.mkdir(os.path.join(user_dir, "Test"))
        FormatConverter.convert_feeds([TestFormatConverter.parsed_feed], "html", os.path.join(user_dir, "Test"), False)
        self.assertEqual(count_files_by_type(os.path.join(user_dir, "Test"), ".html"), 1)
        shutil.rmtree(os.path.join(user_dir, "Test"))
        os.mkdir(os.path.join(user_dir, "Test"))
        FormatConverter.convert_feeds([TestFormatConverter.parsed_feed], "epub", os.path.join(user_dir, "Test"), False)
        self.assertEqual(count_files_by_type(os.path.join(user_dir, "Test"), ".epub"), 1)
        shutil.rmtree(os.path.join(user_dir, "Test"))

    def test_single_feed_to_html_content(self):
        self.assertEqual(type(FormatConverter.single_feed_to_html_content(TestFormatConverter.parsed_feed, True)), str)
        self.assertEqual(
            type(FormatConverter.single_feed_to_html_content(TestFormatConverter.parsed_feed, False)), str)


unittest.main()
