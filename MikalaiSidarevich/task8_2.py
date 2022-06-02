# Task 8.2
# Write end-to-end test for task 7.6.

import task7_6
import unittest.mock


class TestTask76(unittest.TestCase):
    """End-to-end testcase for task76."""

    @unittest.mock.patch('builtins.print', side_effect=StopIteration)
    @unittest.mock.patch('builtins.input')
    def test_main(self, mock_input, mock_print):
        """
        task76.main() test. input() and print() functions are mocked.
        """
        values = {'10': "Goldbach's conjecture: 10 = 3 + 7",
                  '11': "Error: number should be even",
                  '2': "Error: number should be >= 4",
                  '2.5': "Error: invalid literal for int() with base 10: '2.5'",
                  'hello': "Error: invalid literal for int() with base 10: 'hello'",
                  'q': ""}

        for i, (k, v) in enumerate(values.items()):
            mock_input.return_value = k
            try:
                task7_6.main()
            except StopIteration:
                value = mock_print.mock_calls[i]
                expected_value = unittest.mock.call(v)
                self.assertEqual(value, expected_value)


if __name__ == '__main__':
    unittest.main()
