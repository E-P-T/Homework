"""
This module contains one class aimed at testing work of task2.
"""


import task_2
import unittest


class CountStringCharactersTest(unittest.TestCase):
    """
    This class contains some tests for each function of task2.
    """
    def test_count_string_characters(self):
        self.assertEqual(
            task_2.count_string_characters('Hello world!'),
            {
                'h': 1, 'e': 1, 'l': 3, 'o': 2,
                'w': 1, 'r': 1, 'd': 1, ' ': 1, '!': 1
            }
        )

    def test_count_string_characters2(self):
        self.assertEqual(
            task_2.count_string_characters2('Hello world!'),
            {
                'h': 1, 'e': 1, 'l': 3, 'o': 2,
                'w': 1, 'r': 1, 'd': 1, ' ': 1, '!': 1
            }
        )

    def test_count_string_characters3(self):
        self.assertEqual(
            task_2.count_string_characters3('Hello world!'),
            {
                'h': 1, 'e': 1, 'l': 3, 'o': 2,
                'w': 1, 'r': 1, 'd': 1, ' ': 1, '!': 1
            }
        )

    def test_count_string_characters4(self):
        self.assertEqual(
            task_2.count_string_characters4('Hello world!'),
            {
                'h': 1, 'e': 1, 'l': 3, 'o': 2,
                'w': 1, 'r': 1, 'd': 1, ' ': 1, '!': 1
            }
        )
