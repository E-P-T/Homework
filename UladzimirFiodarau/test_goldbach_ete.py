import unittest
from unittest.mock import patch, call
import goldbach


class TestGoldbach(unittest.TestCase):

    @patch('builtins.print')
    @patch('goldbach.get_input')
    def test_main(self, mock_input, mock_print):
        mock_input.side_effect = ['r', '10', '', '20', '0', '-5', '6', 'q']
        goldbach.main()
        self.assertEqual(mock_print.mock_calls,
                         [call('Incorrect input: Wrong argument type, must be an integer'),
                          call((10, [7, 3])),
                          call('Incorrect input: Function requires directly one integer argument'),
                          call((20, [17, 3])),
                          call("Incorrect input: Input integer doesn't satisfy conjecture assumings"),
                          call("Incorrect input: Input integer doesn't satisfy conjecture assumings"),
                          call((6, [3, 3])),
                          call('Thanks for using script and have a good day')
                          ])


if __name__ == '__main__':
    unittest.main()
