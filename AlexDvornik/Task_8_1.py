"""
Task 8.1
Using mock write unit test for task 7.6.
"""
import unittest.mock
from testing_task import Goldbach


class GoldbachTestCase(unittest.TestCase):

    @unittest.mock.patch('testing_task.Goldbach.is_prime')
    def test_is_prime(self, mocked_method):
        n = 5
        Goldbach.is_prime(n)
        self.assertTrue(mocked_method.called)
