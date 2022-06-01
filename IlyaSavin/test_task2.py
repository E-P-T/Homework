#! /usr/bin/env python


"""
This module contains one class aimed at testing work of task2.
"""


import unittest
import task_2


class TestMostCommonWords(unittest.TestCase):
    """
    This class contains some tests for each function of task2.
    """
    def test_most_common_words(self):
        self.assertEqual(
            task_2.most_common_words("data/lorem_ipsum.txt"),
            ['donec', 'etiam', 'aliquam']
        )
        self.assertEqual(
            task_2.most_common_words("data/lorem_ipsum.txt", 5),
            ['donec', 'etiam', 'aliquam', 'aenean', 'maecenas']
        )

    def test_most_common_words2(self):
        self.assertEqual(
            task_2.most_common_words2("data/lorem_ipsum.txt"),
            ['donec', 'etiam', 'aliquam']
        )
        self.assertEqual(
            task_2.most_common_words2("data/lorem_ipsum.txt", 5),
            ['donec', 'etiam', 'aliquam', 'aenean', 'maecenas']
        )
