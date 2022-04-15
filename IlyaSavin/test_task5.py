"""
This module contains one class aimed at testing work of task5.
"""


import task_5
import unittest


class TestGetSortedDictByKey(unittest.TestCase):
    """
    This class contains some tests for each function of task5.
    This class can't check function sort_dict_by_key because it change
    source dictionary. Unit-testing doesn't cover side effects functions.
    """
    def test_get_sorted_by_key_dict(self):
        self.assertEqual(
            task_5.get_sorted_by_key_dict({2: 'two', 3: 'three', 1: 'one'}),
            {1: 'one', 2: 'two', 3: 'three'}
        )

        self.assertEqual(
            task_5.get_sorted_by_key_dict({3: 'three', 2: 'two', 1: 'one'}),
            {1: 'one', 2: 'two', 3: 'three'}
        )
