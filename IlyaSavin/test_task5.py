#! /usr/bin/env python

"""
This module contains one class aimed at testing work of task5.
"""


import unittest
import task_5


class TestGetDigits(unittest.TestCase):
    """
    This class contains some tests for each function of task5.
    """
    def test_get_digits_genexpr(self):
        self.assertEqual(
            task_5.get_digits_genexpr(123456789),
            (1, 2, 3, 4, 5, 6, 7,  8, 9)
        )
        self.assertEqual(
            task_5.get_digits_genexpr(111111111),
            (1, 1, 1, 1, 1, 1, 1, 1, 1)
        )
        self.assertNotEqual(
            task_5.get_digits_genexpr(123123123),
            (1, 2, 3)
        )
        self.assertTupleEqual(
            task_5.get_digits_genexpr(123456789),
            (1, 2, 3, 4, 5, 6, 7,  8, 9)
        )

    def test_get_digits_listcmp(self):
        self.assertEqual(
            task_5.get_digits_listcmp(123456789),
            (1, 2, 3, 4, 5, 6, 7,  8, 9)
        )
        self.assertEqual(
            task_5.get_digits_listcmp(111111111),
            (1, 1, 1, 1, 1, 1, 1, 1, 1)
        )
        self.assertNotEqual(
            task_5.get_digits_listcmp(123123123),
            (1, 2, 3)
        )
        self.assertTupleEqual(
            task_5.get_digits_listcmp(123456789),
            (1, 2, 3, 4, 5, 6, 7,  8, 9)
        )
