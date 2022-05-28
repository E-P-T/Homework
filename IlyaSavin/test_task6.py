#! /usr/bin/env python


"""
This module contains one class aimed at testing work of task6.
"""


import unittest
import task_6


class TestGetLongestWord(unittest.TestCase):
    """
    This class contains some tests for each function of task6.
    """
    def test_get_longest_word(self):
        self.assertEqual(
            task_6.get_longest_word("Hi world I'm an engineer and I'm tired"),
            'engineer'
        )
        self.assertEqual(
            task_6.get_longest_word("Any pythonista like namespaces a lot."),
            'pythonista'
        )

    def test_get_longest_word2(self):
        self.assertEqual(
            task_6.get_longest_word2("Hi world I'm an engineer and I'm tired"),
            'engineer'
        )
        self.assertEqual(
            task_6.get_longest_word2("Any pythonista like namespaces a lot."),
            'pythonista'
        )
