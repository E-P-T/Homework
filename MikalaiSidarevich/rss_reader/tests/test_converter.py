"""Test Converter class."""

from unittest import TestCase

from engine.converter import Converter


class TestConverter(TestCase):
    """Testcase for Converter class."""

    def test_to_text(self):
        """
        to_text() test.
        """
        feed = {'channel': "",
                'entries': [{'title': "",
                             'date': "",
                             'link': "",
                             'description': "",
                             'image_link': ""}]}
        self.assertIsNotNone(Converter.to_text(feed))

    def test_to_json(self):
        """
        to_json() test.
        """
        feed = {'channel': "",
                'entries': [{'title': "",
                             'date': "",
                             'link': "",
                             'description': "",
                             'image_link': ""}]}
        self.assertIsNotNone(Converter.to_json(feed))
