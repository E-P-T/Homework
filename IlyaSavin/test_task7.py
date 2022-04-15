"""
This module contains one class aimed at testing work of task7.
"""

import task_7
import unittest


class TestTupleToNumber(unittest.TestCase):
    """
    This class contains some tests for each function of task7.
    """
    def test_tuple_to_number_cmp(self):
        self.assertEqual(task_7.tuple_to_number_cmp((1, 2, 3)), 123)
        self.assertEqual(task_7.tuple_to_number_cmp((1, 0, 3, 0, 1)), 10301)

    def test_tuple_to_number(self):
        self.assertEqual(task_7.tuple_to_number((1, 2, 3)), 123)
        self.assertEqual(task_7.tuple_to_number((1, 0, 3, 0, 1)), 10301)
