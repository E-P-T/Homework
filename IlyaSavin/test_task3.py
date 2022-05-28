#! /usr/bin/env python


"""
This module contains one class aimed at testing work of task3.
"""


import unittest
import task_3


class TestSplit(unittest.TestCase):
    """
    This class contains some tests for each function of task3.
    """
    def test_split_iterable(self):
        self.assertEqual(
            task_3.split_iterable('Hello world how are you'),
            ['Hello', 'world', 'how', 'are', 'you']
        )
        self.assertEqual(
            task_3.split_iterable('Hello#world#how#are#you', sep='#'),
            ['Hello', 'world', 'how', 'are', 'you']
        )
        self.assertEqual(
            task_3.split_iterable('Hello world how are you', maxsplit=3),
            ['Hello', 'world', 'how', 'are you']
        )
        self.assertEqual(
            task_3.split_iterable('Hello#world#how#are#you', sep='#', maxsplit=3),
            ['Hello', 'world', 'how', 'are#you']
        )

    def test_split_recursion(self):
        self.assertEqual(
            task_3.split_recursion('Hello world how are you'),
            ['Hello', 'world', 'how', 'are', 'you']
        )
        self.assertEqual(
            task_3.split_recursion('Hello#world#how#are#you', sep='#'),
            ['Hello', 'world', 'how', 'are', 'you']
        )
        self.assertEqual(
            task_3.split_recursion('Hello world how are you', maxsplit=3),
            ['Hello', 'world', 'how', 'are you']
        )
        self.assertEqual(
            task_3.split_recursion('Hello#world#how#are#you', sep='#', maxsplit=3),
            ['Hello', 'world', 'how', 'are#you']
        )
