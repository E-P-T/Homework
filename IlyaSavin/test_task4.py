#! /usr/bin/env python

"""
This module contains one class aimed at testing work of task4.
"""


import unittest
import task_4


class TestSplitByIndex(unittest.TestCase):
    """
    This class contains some tests for each function of task4.
    """
    def test_split_by_index(self):
        self.assertEqual(
            task_4.split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]),
            ["python", "is", "cool", ",", "isn't", "it?"]
        )
        self.assertEqual(
            task_4.split_by_index("Splitmeplease", [5, 7, 99, 10, 18]),
            ["Split", "me", "ple", "ase"]
        )
        self.assertNotEqual(
            task_4.split_by_index("no luck", [42]),
            ["no", "luck"]
        )

    def test_split_by_index_rec(self):
        self.assertEqual(
            task_4.split_by_index_rec("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]),
            ["python", "is", "cool", ",", "isn't", "it?"]
        )
        self.assertEqual(
            task_4.split_by_index_rec("Splitmeplease", [5, 7, 99, 10, 18]),
            ["Split", "me", "ple", "ase"]
        )
        self.assertNotEqual(
            task_4.split_by_index_rec("no luck", [42]),
            ["no", "luck"]
        )
