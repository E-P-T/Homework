"""
This module contains one class aimed at testing work of task6.
"""

import task_6
import unittest


class TestGetListOfUniqueValues(unittest.TestCase):
    """
    This class contains some tests for each function of task6.
    """
    def test_get_list_of_unique_values(self):
        self.assertEqual(
            task_6.get_list_of_unique_values(
                [
                    {"V": "S001"}, {"V": "S002"},
                    {"VI": "S001"}, {"VI": "S005"},
                    {"VII": "S005"}, {"V": "S009"},
                    {"VIII": "S007"}
                 ]
            ),
            ['S001', 'S002', 'S005', 'S007', 'S009']
        )
        self.assertNotEqual(
            task_6.get_list_of_unique_values(
                [
                    {"V": "S001"}, {"V": "S002"},
                    {"VI": "S001"}, {"VI": "S005"},
                    {"VII": "S005"}, {"V": "S009"},
                    {"VIII": "S007"}
                 ]
            ),
            ('S001', 'S002', 'S005', 'S007', 'S009')
        )

    def test_get_list_of_unique_values_cmp(self):
        self.assertEqual(
            task_6.get_list_of_unique_values_cmp(
                [
                    {"V": "S001"}, {"V": "S002"},
                    {"VI": "S001"}, {"VI": "S005"},
                    {"VII": "S005"}, {"V": "S009"},
                    {"VIII": "S007"}
                 ]
            ),
            ['S001', 'S002', 'S005', 'S007', 'S009']
        )
        self.assertNotEqual(
            task_6.get_list_of_unique_values_cmp(
                [
                    {"V": "S001"}, {"V": "S002"},
                    {"VI": "S001"}, {"VI": "S005"},
                    {"VII": "S005"}, {"V": "S009"},
                    {"VIII": "S007"}
                 ]
            ),
            ('S001', 'S002', 'S005', 'S007', 'S009')
        )
