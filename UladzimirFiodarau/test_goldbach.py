# Task 8.1
# Using mock write unit test for task 7.6.
import unittest
from unittest.mock import patch, call
import goldbach


class TestGoldbach(unittest.TestCase):

    def test_CustomException(self):
        self.assertEqual(str(goldbach.CustomException('Custom message')), 'Custom message')
        self.assertEqual(str(goldbach.CustomException()), '')
        self.assertEqual(str(goldbach.CustomException(50)), '50')
        self.assertEqual(str(goldbach.CustomException(True)), 'True')

    def test_is_even(self):
        self.assertTrue(goldbach.is_even(0))
        self.assertTrue(goldbach.is_even(2))
        self.assertTrue(goldbach.is_even(-2))
        self.assertFalse(goldbach.is_even(3))
        self.assertFalse(goldbach.is_even(-3))
        with self.assertRaises(goldbach.EmptyException):
            goldbach.is_even()
        with self.assertRaises(goldbach.EmptyException):
            goldbach.is_even(None)
        with self.assertRaises(goldbach.TypeException):
            goldbach.is_even('string')
        with self.assertRaises(goldbach.TypeException):
            goldbach.is_even('')
        with self.assertRaises(goldbach.TypeException):
            goldbach.is_even('10')
        with self.assertRaises(goldbach.TypeException):
            goldbach.is_even([])
        with self.assertRaises(goldbach.TypeException):
            goldbach.is_even([1, 3, 5])
        with self.assertRaises(goldbach.TypeException):
            goldbach.is_even({'a': 6, 'b': 8})
        with self.assertRaises(goldbach.TypeException):
            goldbach.is_even(2.5)

    def test_get_primes(self):
        with self.assertRaises(AssertionError):
            goldbach.get_primes(2.5)
        with self.assertRaises(AssertionError):
            goldbach.get_primes('10')
        with self.assertRaises(goldbach.EmptyException):
            goldbach.get_primes(None)
        with self.assertRaises(goldbach.EmptyException):
            goldbach.get_primes()
        with self.assertRaises(AssertionError):
            goldbach.get_primes(-1)
        with self.assertRaises(AssertionError):
            goldbach.get_primes(-14)
        self.assertEqual(goldbach.get_primes(0), [])
        self.assertEqual(goldbach.get_primes(1), [])
        self.assertEqual(goldbach.get_primes(2), [2])
        self.assertEqual(goldbach.get_primes(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

    def test_find_goldbach(self):
        self.assertEqual(goldbach.find_goldbach(10), (10, [7, 3]))
        self.assertEqual(goldbach.find_goldbach(4), (4, [2, 2]))
        self.assertEqual(goldbach.find_goldbach(10000), (10000, [9941, 59]))
        with self.assertRaises(goldbach.ValueException):
            goldbach.find_goldbach(-14)
        with self.assertRaises(goldbach.ValueException):
            goldbach.find_goldbach(-15)
        with self.assertRaises(goldbach.ValueException):
            goldbach.find_goldbach(0)

    @patch('goldbach.is_even')
    @patch('goldbach.get_primes')
    def test_find_goldbach_mock(self, mock_primes, mock_is_even):
        mock_is_even.return_value = True
        mock_primes.return_value = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(goldbach.find_goldbach(50), (50, [47, 3]))

        mock_is_even.return_value = True
        mock_primes.return_value = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
        self.assertEqual(goldbach.find_goldbach(50), (50, [43, 7]))

        mock_is_even.return_value = False
        mock_primes.return_value = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        with self.assertRaises(goldbach.ValueException):
            goldbach.find_goldbach(50)

    @patch('builtins.print')
    @patch('goldbach.get_input')
    def test_main(self, mock_input, mock_print):
        mock_input.return_value = 'q'
        goldbach.main()
        self.assertEqual(mock_print.mock_calls, [call('Thanks for using script and have a good day')])


if __name__ == '__main__':
    unittest.main()
