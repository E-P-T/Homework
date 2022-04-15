"""
This module contains one class aimed at testing work of task1.
"""


import task_1
import unittest


class GetLengthTest(unittest.TestCase):
    """
    This class contains some tests for each function of task1.
    """
    def test_get_length_genexpr(self):
        self.assertEqual(task_1.get_length_genexpr('Hello'), 5)

    def test_get_length_listcmp(self):
        self.assertEqual(task_1.get_length_listcmp('Hello'), 5)

    def test_get_length_loopfor(self):
        self.assertEqual(task_1.get_length_loopfor('Hello'), 5)

    def test_get_length_loopwhile(self):
        self.assertEqual(task_1.get_length_loopwhile('Hello'), 5)

    def test_raised_exc_genexpr(self):
        self.assertRaises(TypeError, task_1.get_length_genexpr, 50)

    def test_raised_exc_listcmp(self):
        self.assertRaises(TypeError, task_1.get_length_listcmp, 50)

    def test_raised_exc_loopfor(self):
        self.assertRaises(TypeError, task_1.get_length_loopfor, 50)

    def test_raised_exc_loopwhile(self):
        self.assertRaises(TypeError, task_1.get_length_loopwhile, 50)
