import unittest
from unittest.mock import patch, call
import goldbachprogram

class TestGoldbach(unittest.TestCase):

    @patch('goldbachprogram.userInput')
    @patch('builtins.print')
    def test_consoleProgram(self, mock_print, mock_input):
        mock_input.side_effect = ['10', 'word', '4', '-10', '21', '1000', 'q']
        goldbachprogram.consoleProgram()
        self.assertEqual(mock_print.mock_calls,
                         [call([10, [3, 7]]),
                          call('Error: Unsupported argument type. Argument must be integer'),
                          call([4, [2, 2]]),
                          call('Error: Argument is not supported. Please read homework'),
                          call('Error: Argument is not supported. Please read homework'),
                          call([1000, [3, 997]]),
                          call('You quitted program. Bye-bye')
                          ])

unittest.main()
