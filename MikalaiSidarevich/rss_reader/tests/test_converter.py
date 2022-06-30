"""Test Converter class."""

from unittest import TestCase
from unittest.mock import patch

from engine.converter import Converter


class TestConverter(TestCase):
    """Testcase for Converter class."""

    def test_to_text(self):
        """
        to_text() test.
        """
        feed_list = [{'channel': "",
                      'entries': [{'title': "",
                                   'date': "",
                                   'link': "",
                                   'description': "",
                                   'image_link': ""}]}]
        self.assertIsNotNone(Converter.to_text(feed_list))

    def test_to_json(self):
        """
        to_json() test.
        """
        feed_list = [{'channel': "",
                      'entries': [{'title': "",
                                   'link': "",
                                   'date_fmt': "",
                                   'image_data': ""}]}]
        self.assertIsNotNone(Converter.to_json(feed_list))

    @patch('builtins.open')
    def test_save_html(self, mock_open):
        """
        save_html() test.
        """
        feeds = [{'channel': "",
                  'url': "",
                  'entries': [{'title': "",
                               'date': "",
                               'date_fmt': "",
                               'link': "",
                               'description': "",
                               'image_link': "",
                               'image_data': b""}]}]
        with self.assertRaises(Exception):
            Converter.save_html(feeds, "1/")

    @patch('ebooklib.epub.EpubWriter.write')
    def test_save_epub(self, mock_write):
        """
        save_epub() test.
        """
        feeds = [{'channel': "",
                  'url': "",
                  'entries': [{'title': "",
                               'date': "",
                               'date_fmt': "",
                               'link': "",
                               'description': "",
                               'image_link': "",
                               'image_data': b""}]}]
        Converter.save_epub(feeds, "")
        mock_write.assert_called_once()
