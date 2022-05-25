"""
Using mock write unit test for task 7.6.
"""

import unittest
from unittest.mock import MagicMock
import Task7_6

class TestGoldbach (unittest.TestCase):

    @ staticmethod
    def mock_even(num):
        if not isinstance(num, int):
            return False
        elif num<3:
            return False
        elif num % 2 == 1:
            return False
        else:
            return True

    def test_conjecture (self):
        Task7_6.if_even = MagicMock(side_effect = self.mock_even)

        test_cases = [{'argum': 5.6, 'expect':None},
        {'argum': 8, 'expect': [3,5]},
        {'argum': 7, 'expect':None},
        {'argum': 10, 'expect':[3,7]},
        {'argum': 'q', 'expect':None}]

        for test_case in test_cases:
            result = Task7_6.conjecture(test_case['argum'])
            exp_val = test_case['expect']
            self.assertEqual(result, exp_val)

if __name__ == '__main__':
    unittest.main()