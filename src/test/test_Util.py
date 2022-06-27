import datetime
import json
from unittest import TestCase
from Util import Util
from colorama import Fore


class TestUtil(TestCase):
    def test_colorize(self):
        string = 'dsa'
        self.assertRegex(Util.colorize(string, Fore.GREEN), string)

    def test_safe_vars(self):
        for item in ['a', {'a': 'a'}, self, datetime.date.today()]:
            try:
                Util.safe_vars(item)
            except:
                self.fail()

    def test_to_json(self):
        obj = {'a': 1, 'b': 2}
        self.assertEqual(obj, json.loads(Util.to_json(obj)))

    def test_make_intend(self):
        string = 'test'
        self.assertEqual(Util.make_indent(string), Util.indent + string)

    def test_unique(self):
        unique = [1, 2, 3, 4, 5]
        self.assertEqual(unique, Util.unique(unique + [1, 2, 4]))

    def test_regex(self):
        string = 'test'
        pattern = '^t'
        replace = 'the t'
        self.assertEqual(Util.regex(pattern, replace, string), 'the ' + string)
