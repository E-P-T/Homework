"""Test Converter class."""

from unittest import TestCase

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
