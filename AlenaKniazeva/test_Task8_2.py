"""
Write end-to-end test for task 7.6.
"""

import unittest
from unittest import mock
from unittest.mock import patch
import io

import Task7_6

class TestGoldbach (unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('Task7_6.input_num')
    def test_goldbachE2E (self, mock_input, mock_stdout):
        test_cases = ['5.6', '8','2', '7', 'q']
        expected_output = "It's not a number!"+"\n"+\
            "Components of Goldbach's conjecture: [3, 5]"+"\n"+\
            "Error: The number is less than 3"+"\n"+\
            "Error: The number is not an even number"+"\n"+\
            "Quit"+"\n"
        mock_input.side_effect = test_cases
        Task7_6.main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()