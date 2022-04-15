"""
This module contains one class aimed at testing work of task3.
"""


import task_3
import unittest


class TestPrintUniqueSortedWords(unittest.TestCase):
    """
    This class contains some tests for each function of task3.
    """
    def test_print_unique_sorted_words(self):
        self.assertEqual(
            task_3.print_uniq_sorted_words(
                ('red', 'white', 'black', 'red', 'green', 'black')
            ),
            ('black', 'green', 'red', 'white')
        )

        self.assertNotEqual(
            task_3.print_uniq_sorted_words(
                ('red', 'white', 'black', 'red', 'green', 'black')
            ),
            ['black', 'green', 'red', 'white']
        )

    def test_print_unique_sorted_words2(self):
        self.assertEqual(
            task_3.print_uniq_sorted_words2(
                ['red', 'white', 'black', 'red', 'green', 'black']
            ),
            ['black', 'green', 'red', 'white']
        )

        self.assertNotEqual(
            task_3.print_uniq_sorted_words2(
                ['red', 'white', 'black', 'red', 'green', 'black']
            ),
            ('black', 'green', 'red', 'white')
        )
