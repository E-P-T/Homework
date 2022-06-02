# Task 8.1
# Using mock write unit test for task 7.6.

import task7_6
import unittest.mock


class TestTask76(unittest.TestCase):
    """Testcase for task76."""

    def test_is_even(self):
        """
        task76.is_even() test.
        """
        self.assertFalse(task7_6.is_even(1))
        self.assertTrue(task7_6.is_even(2))
        with self.assertRaises(task7_6.FloatException):
            task7_6.is_even(2.5)
        with self.assertRaises(task7_6.StringException):
            task7_6.is_even("2.5")
        with self.assertRaises(task7_6.ListException):
            task7_6.is_even([2])
        with self.assertRaises(Exception):
            task7_6.is_even({2})

    def test_is_prime(self):
        """
        task76.is_prime() test.
        """
        self.assertFalse(task7_6.is_prime(1))
        self.assertTrue(task7_6.is_prime(2))
        self.assertTrue(task7_6.is_prime(3))
        self.assertFalse(task7_6.is_prime(4))
        self.assertTrue(task7_6.is_prime(5))

    def test_goldbach(self):
        """
        task76.goldbach() test.
        """
        with self.assertRaises(task7_6.EvenError):
            task7_6.goldbach(5)
        with self.assertRaises(ValueError):
            task7_6.goldbach(2)
        self.assertEqual(task7_6.goldbach(10), [3, 7])

    @unittest.mock.patch('task7_6.main')
    def test_main(self, mock_main):
        """
        task76.main() test, function is mocked.
        """
        task7_6.main()
        self.assertTrue(mock_main.called)


if __name__ == '__main__':
    unittest.main()
