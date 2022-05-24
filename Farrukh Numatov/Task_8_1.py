"""Using mock write unit test for task 7.6."""
import unittest
from unittest.mock import patch
from Task_7_6 import goldbach
from Task_7_5 import even_checker


class MyTest(unittest.TestCase):
    def test_even_1(self):
        self.assertTrue(even_checker("4"))
        self.assertFalse(even_checker("3"))
        self.assertTrue(even_checker("5"))

    def test_even_2(self):
        exc_cases = ["asd", "0", "1.25", "10"]
        for case in exc_cases:
            with self.assertRaises(Exception):
                even_checker(case)

    def test_goldbach(self):
        self.assertEqual(goldbach(4), (1, 3))
        self.assertEqual(goldbach(10), (5, 5))
        self.assertEqual(goldbach(10), (3, 7))

    @patch('Task_7_5.even_checker')
    def test_for_isalpha(self, mock_isalpha):
        mock_isalpha.return_value = False
        with self.assertRaises(Exception):
            even_checker("al")
            mock_isalpha.assert_called_once()


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
