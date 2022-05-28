#! /usr/bin/env python


"""
This module contains one class aimed at testing work of task11.
"""


import unittest
import task_11


class TestCombineDicits(unittest.TestCase):
    """
    This class contains some tests for each function of task11.
    """
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    def test_combine_dicits(self):
        self.assertEqual(
            task_11.combine_dicts(
                TestCombineDicits.dict_1,
                TestCombineDicits.dict_2
            ),
            {'a': 300, 'b': 200, 'c': 300}
        )
        self.assertEqual(
            task_11.combine_dicts(
                TestCombineDicits.dict_1,
                TestCombineDicits.dict_2,
                TestCombineDicits.dict_3
            ),
            {'a': 600, 'b': 200, 'c': 300, 'd': 100}
        )

    def test_combine_dicits2(self):
        self.assertEqual(
            task_11.combine_dicts2(
                TestCombineDicits.dict_1,
                TestCombineDicits.dict_2
            ),
            {'a': 300, 'b': 200, 'c': 300}
        )
        self.assertEqual(
            task_11.combine_dicts2(
                TestCombineDicits.dict_1,
                TestCombineDicits.dict_2,
                TestCombineDicits.dict_3
            ),
            {'a': 600, 'b': 200, 'c': 300, 'd': 100}
        )
