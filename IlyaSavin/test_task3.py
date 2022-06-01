#! /usr/bin/env python


"""
This module contains one class aimed at testing work of task3.
"""


import unittest
import task_3


class TestGetTopPerformers(unittest.TestCase):
    """
    This class contains some tests for each function of task3.
    """
    def test_get_top_performers(self):
        self.assertEqual(
            task_3.get_top_performers("data/students.csv"),
            [
                'Josephina Medina', 'Richard Snider', 'Teresa Jones',
                'Heather Garcia', 'Jessica Dubose'
            ]
        )
        self.assertEqual(
            task_3.get_top_performers("data/students.csv", 6),
            [
                'Josephina Medina', 'Richard Snider', 'Teresa Jones',
                'Heather Garcia', 'Jessica Dubose',  'Joseph Head'
            ]
        )

    def test_get_top_performers2(self):
        self.assertEqual(
            task_3.get_top_performers2("data/students.csv"),
            [
                'Josephina Medina', 'Teresa Jones', 'Richard Snider',
                'Jessica Dubose', 'Heather Garcia'
            ]
        )
        self.assertEqual(
            task_3.get_top_performers2("data/students.csv", 6),
            [
                'Josephina Medina', 'Teresa Jones', 'Richard Snider',
                'Jessica Dubose', 'Heather Garcia', 'Joseph Head'
            ]
        )
