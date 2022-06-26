import unittest.mock
import unittest
import task7_6 as task


class TestForTask(unittest.TestCase):
    """Test case for Task 7.6"""

    def test_is_even(self):
        """Method for testing is_even method"""

        self.assertFalse(task.is_even(1))
        self.assertTrue(task.is_even(2))

        with self.assertRaises(task.StringException):
            task.is_even("3")
        with self.assertRaises(task.NotIntegerException):
            task.is_even(2.5)

    def test_gen_prime(self):
        """Method for testing gen_prime method"""
        self.assertEqual(task.gen_primes(10), [2, 3, 5, 7])

    def test_goldbach(self):
        """Method for testing gen_prime method"""
        self.assertEqual(task.goldbach(10), [(3, 7), (5, 5), (7, 3)])

    @unittest.mock.patch('task7_6.main')
    def test_main(self, mock_main):
        """
        task76.main() test, function is mocked.
        """
        task.main()
        self.assertTrue(mock_main.called)


if __name__ == "__main__":
    unittest.main()
