import json
from unittest import TestCase

from rss_reader.src.util.Util import Util


class TestUtil(TestCase):
    def test_to_json(self):
        obj = {
            'title': 'Title',
            'link': 'Link',
            'description': 'Description'
        }

        self.assertEqual(
            obj,
            json.loads(Util.to_json(obj))
        )
