"""Test ArgParser class."""

from unittest import TestCase

from engine.argparser import ArgParser


class TestArgParser(TestCase):
    """Testcase for ArgParser class."""

    def setUp(self):
        """
        Prepare test fixture.
        """
        self.parser = ArgParser()

    def test_args(self):
        """
        args-property test.
        """
        expected = {'source': None,
                    'version': False,
                    'json': False,
                    'verbose': False,
                    'limit': None,
                    'date': None,
                    'to_html': None,
                    'to_epub': None}
        self.assertDictEqual(self.parser.args, expected)
