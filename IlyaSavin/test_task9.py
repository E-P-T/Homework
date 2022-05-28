#! /usr/bin/env python


"""
This module contains one class aimed at testing work of task9.
"""


import unittest
import task_9


class TestFunctions(unittest.TestCase):
    """
    This class contains some tests for each function of task9.
    """
    test_strings = ["hello", "world", "python", ]
    test_strings2 = ['hii', 'how are youi?', 'helicopter']

    def test_1_1(self):
        self.assertEqual(task_9.test_1_1(*TestFunctions.test_strings), {'o'})
        self.assertEqual(task_9.test_1_1(*TestFunctions.test_strings2), {'h', 'i'})

    def test_1_2(self):
        self.assertEqual(
            task_9.test_1_2(*TestFunctions.test_strings),
            {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
        )
        self.assertEqual(
            task_9.test_1_2(*TestFunctions.test_strings2),
            {'h', 'i', 'o', 'w', 'a', 'r', 'e', 'y', 'u', 'l', 'c', 'p', 't'}
        )

    def test_1_3(self):
        self.assertEqual(
            task_9.test_1_3(*TestFunctions.test_strings),
            {'h', 'l', 'o'}
        )
        self.assertEqual(
            task_9.test_1_3(*TestFunctions.test_strings2),
            {'h', 'i', 'r', 'e', 'o'}
        )

    def test_1_4(self):
        self.assertEqual(
            task_9.test_1_4(*TestFunctions.test_strings),
            {'a', 'b', 'c', 'f', 'g', 'i', 'j',
             'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
        )
        self.assertEqual(
            task_9.test_1_4(*TestFunctions.test_strings2),
            {'z', 'q', 'g', 'f', 'm', 's', 'v',
             'j', 'd', 'n', 'b', 'x', 'k'}
        )

    def test_1_1_2(self):
        self.assertEqual(task_9.test_1_1_2(*TestFunctions.test_strings), {'o'})
        self.assertEqual(task_9.test_1_1_2(*TestFunctions.test_strings2), {'h', 'i'})

    def test_1_2_2(self):
        self.assertEqual(
            task_9.test_1_2_2(*TestFunctions.test_strings),
            {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
        )
        self.assertEqual(
            task_9.test_1_2_2(*TestFunctions.test_strings2),
            {'h', 'i', 'o', 'w', 'a', 'r', 'e', 'y', 'u', 'l', 'c', 'p', 't'}
        )

    def test_1_3_2(self):
        self.assertEqual(
            task_9.test_1_3_2(*TestFunctions.test_strings),
            {'h', 'l', 'o'}
        )
        self.assertEqual(
            task_9.test_1_3_2(*TestFunctions.test_strings2),
            {'h', 'i', 'r', 'e', 'o'}
        )

    def test_1_4_2(self):
        self.assertEqual(
            task_9.test_1_4_2(*TestFunctions.test_strings),
            {'a', 'b', 'c', 'f', 'g', 'i', 'j',
             'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
        )
        self.assertEqual(
            task_9.test_1_4_2(*TestFunctions.test_strings2),
            {'z', 'q', 'g', 'f', 'm', 's', 'v',
             'j', 'd', 'n', 'b', 'x', 'k'}
        )
