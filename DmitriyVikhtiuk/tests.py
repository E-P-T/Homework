import unittest
from main import *
from unittest.mock import patch


class TestGoldbach(unittest.TestCase):

    def test_prime_for_even(self):
        self.assertEqual(type(prime_for_even(10)), list)
        self.assertEqual(prime_for_even(4), [2, 2])
        self.assertEqual(prime_for_even(6), [3, 3])
        self.assertEqual(prime_for_even(60), [7, 53])

    def test_prime_nums(self):
        self.assertEqual(type(prime_nums(10)), list)
        self.assertTrue(prime_nums(4))
        self.assertTrue(prime_nums(7))
        self.assertTrue(prime_nums(10))
        self.assertFalse(prime_nums(-5))
        self.assertFalse(prime_nums(0))


    def test_prime_for_not_even(self):
        self.assertEqual(type(prime_for_even(11)), list)
        self.assertEqual(prime_for_not_even(7), [3, 2, 2])
        self.assertEqual(prime_for_not_even(9), [3, 3, 3])
        self.assertEqual(prime_for_not_even(91), [3, 5, 83])

    @patch('main.prime_for_even')
    def test_prime_for_even_mock(self, mock_prime_nums):
        mock_prime_nums.return_value = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(prime_for_even(18), [5, 13])


    @patch('main.prime_for_not_even')
    def test_prime_for_not_even_mock(self, mock_prime_nums):
        mock_prime_nums.return_value = [2, 3, 5, 7]
        self.assertEqual(prime_for_not_even(11), [2, 2, 7])

        mock_prime_nums.return_value = [2, 3, 5]
        self.assertEqual(prime_for_not_even(7), [3, 2, 2])





if __name__ == '__main__':
    unittest.main()

