"""
Task 8.2
Write end-to-end test for task 7.6
"""

import unittest.mock
from testing_task import Goldbach
from exceptions import *


class GoldbachTestCase(unittest.TestCase):

    def setUp(self):
        self.goldbach = Goldbach(20)

    @unittest.mock.patch('testing_task.Goldbach.is_valid')
    def test_is_valid(self, mocked_method):
        self.goldbach.is_valid()
        self.assertTrue(mocked_method.called)

    def test_is_valid_result(self):
        self.assertTrue(self.goldbach.is_valid)

    def test_is_valid_str(self):
        with self.assertRaises(WrongTypeOfArgument):
            Goldbach('text').is_valid()

    @unittest.mock.patch('testing_task.Goldbach.is_prime')
    def test_is_prime(self, mocked_method):
        n = 5
        Goldbach.is_prime(n)
        self.assertTrue(mocked_method.called)

    def test_goldbach(self):
        res = self.goldbach.calc()
        self.assertTrue(isinstance(res, tuple))

    def test_goldbach_result(self):
        result = self.goldbach.calc()
        self.assertEqual(result, (3, 17))


