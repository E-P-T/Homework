#! /usr/bin/env python


"""
This module contains one class aimed at testing work of task1.
"""


import unittest
import task_1


class TestStringReplace(unittest.TestCase):
    """
    This class contains some tests for each function of task1.
    """
    def test_replace(self):
        self.assertEqual(
            task_1.replace_quotes("Hello it's John"),
            'Hello it"s John'
        )

        self.assertEqual(
            task_1.replace_quotes("""He told me "I am a gay". Don't blame"""),
            """He told me 'I am a gay'. Don"t blame"""
        )

        self.assertEqual(
            task_1.replace_quotes('"Hello world"'),
            "'Hello world'"
        )

        self.assertNotEqual(
            task_1.replace_quotes("""He told me "I am a gay". Don't blame"""),
            """He told me "I am a gay". Don't blame"""
        )

    def test_replace2(self):

        self.assertEqual(
            task_1.replace_quotes2("Hello it's John"),
            'Hello it"s John'
        )

        self.assertEqual(
            task_1.replace_quotes2("""He told me "I am a gay". Don't blame"""),
            """He told me 'I am a gay'. Don"t blame"""
        )

        self.assertEqual(
            task_1.replace_quotes2('"Hello world"'),
            "'Hello world'"
        )

        self.assertNotEqual(
            task_1.replace_quotes2("""He told me "I am a gay". Don't blame"""),
            """He told me "I am a gay". Don't blame"""
        )
