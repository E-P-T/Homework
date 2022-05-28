#! /usr/bin/env python


"""
This module contains one class aimed at testing work of task7.
"""


import unittest
import task_7


class TestFoo(unittest.TestCase):
    """
    This class contains some tests for each function of task7.
    """
    def test_foo(self):
        self.assertEqual(task_7.foo([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(task_7.foo([3, 2, 1]), [2, 3, 6])

    def test_foo2(self):
        self.assertEqual(task_7.foo2([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(task_7.foo2([3, 2, 1]), [2, 3, 6])

    def test_foo3(self):
        self.assertEqual(task_7.foo3([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(task_7.foo3([3, 2, 1]), [2, 3, 6])
