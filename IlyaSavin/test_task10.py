#! /usr/bin/env python


"""
This module contains one class aimed at testing work of task10.
"""


import unittest
import task_10


class TestGenerateSquares(unittest.TestCase):
    """
    This class contains some tests for each function of task10.
    """
    def test_generate_squares(self):
        self.assertEqual(
            task_10.generate_squares(5),
            {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        )
        self.assertEqual(
            task_10.generate_squares(-5),
            {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        )

    def test_generate_squares2(self):
        self.assertEqual(
            task_10.generate_squares2(5),
            {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        )
        self.assertEqual(
            task_10.generate_squares2(-5),
            {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        )

    def test_generate_squares3(self):
        self.assertEqual(
            task_10.generate_squares3(5),
            {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        )
        self.assertEqual(
            task_10.generate_squares3(-5),
            {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        )
