"""
This module contains one class aimed at testing work of task4.
"""

import task_4
import unittest


class TestGetDivisors(unittest.TestCase):
    """
    This class contains some tests for each function of task4.
    """
    def test_get_divisors(self):
        self.assertEqual(
            task_4.get_divisors(60),
            {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
        )

    def test_get_divisors_setcmp(self):
        self.assertEqual(
            task_4.get_divisors_setcmp(60),
            {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
        )

    def test_get_divisors_listcmp(self):
        self.assertEqual(
            task_4.get_divisors_listcmp(60),
            [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
        )
