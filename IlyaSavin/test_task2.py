#! /usr/bin/env python


"""
This module contains one class aimed at testing work of task2.
"""


import unittest
import task_2


class TestIsPalindrome(unittest.TestCase):
    """
    This class contains some tests for each function of task2.
    """
    def test_is_palindrome_indeces(self):
        self.assertEqual(task_2.is_palindrome_indeces('qwewq'), True)
        self.assertEqual(task_2.is_palindrome_indeces('qweewq'), True)
        self.assertEqual(task_2.is_palindrome_indeces('qwerty'), False)
        self.assertNotEqual(task_2.is_palindrome_indeces('qwerty'), True)

    def test_is_palindrome_loopfor(self):
        self.assertEqual(task_2.is_palindrome_loopfor('qwewq'), True)
        self.assertEqual(task_2.is_palindrome_loopfor('qweewq'), True)
        self.assertEqual(task_2.is_palindrome_loopfor('qwerty'), False)
        self.assertNotEqual(task_2.is_palindrome_loopfor('qwerty'), True)

    def test_is_palindrome_loopwhile(self):
        self.assertEqual(task_2.is_palindrome_loopwhile('qwewq'), True)
        self.assertEqual(task_2.is_palindrome_loopwhile('qweewq'), True)
        self.assertEqual(task_2.is_palindrome_loopwhile('qwerty'), False)
        self.assertNotEqual(task_2.is_palindrome_loopwhile('qwerty'), True)

    def test_is_palindrome_recursion(self):
        self.assertEqual(task_2.is_palindrome_recursion('qwewq'), True)
        self.assertEqual(task_2.is_palindrome_recursion('qweewq'), True)
        self.assertEqual(task_2.is_palindrome_recursion('qwerty'), False)
        self.assertNotEqual(task_2.is_palindrome_recursion('qwerty'), True)

    def test_is_palindrome_genexpr(self):
        self.assertEqual(task_2.is_palindrome_genexpr('qwewq'), True)
        self.assertEqual(task_2.is_palindrome_genexpr('qweewq'), True)
        self.assertEqual(task_2.is_palindrome_genexpr('qwerty'), False)
        self.assertNotEqual(task_2.is_palindrome_genexpr('qwerty'), True)

    def test_is_palindrome_listcomp(self):
        self.assertEqual(task_2.is_palindrome_listcomp('qwewq'), True)
        self.assertEqual(task_2.is_palindrome_listcomp('qweewq'), True)
        self.assertEqual(task_2.is_palindrome_listcomp('qwerty'), False)
        self.assertNotEqual(task_2.is_palindrome_listcomp('qwerty'), True)
