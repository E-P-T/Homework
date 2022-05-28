#! /usr/bin/env python


"""
This module contains one class aimed at testing work of task8.
"""


import unittest
import task_8


class TestGetPairs(unittest.TestCase):
    """
    This class contains some tests for each function of task8.
    """
    def test_get_pairs(self):
        self.assertEqual(
            task_8.get_pairs([1, 2, 3, 8, 9]),
            [(1, 2), (2, 3), (3, 8), (8, 9)]
        )
        self.assertNotEqual(
            task_8.get_pairs([1, 2, 3, 8, 9]),
            None
        )
        self.assertEqual(task_8.get_pairs([1]), None)
        self.assertNotEqual(task_8.get_pairs([1]), [(1, )])

    def test_get_pairs2(self):
        self.assertEqual(
            task_8.get_pairs2([1, 2, 3, 8, 9]),
            [(1, 2), (2, 3), (3, 8), (8, 9)]
        )
        self.assertNotEqual(
            task_8.get_pairs2([1, 2, 3, 8, 9]),
            None
        )
        self.assertEqual(task_8.get_pairs2([1]), None)
        self.assertNotEqual(task_8.get_pairs2([1]), [(1, )])

    def test_get_pairs3(self):
        self.assertEqual(
            task_8.get_pairs3([1, 2, 3, 8, 9]),
            [(1, 2), (2, 3), (3, 8), (8, 9)]
        )
        self.assertNotEqual(
            task_8.get_pairs3([1, 2, 3, 8, 9]),
            None
        )
        self.assertEqual(task_8.get_pairs3([1]), None)
        self.assertNotEqual(task_8.get_pairs3([1]), [(1, )])
