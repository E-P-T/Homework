import unittest
from main import *
from mock import patch, call

class Test_e_2_e(unittest.TestCase):

    @patch('builtins.print')
    @patch('main.get_command')
    def test_main(self, mock_input, mock_print):
        mock_input.side_effect = ['r', '2', '2.5', '10', '5', '20', '2', '3', '6', 'q']
        prog()
        self.assertEqual(mock_print.mock_calls,
                         [call("Invalid type of num. try again"),
                          call("for not even value must be >=7, for even >=4"),
                          call("Invalid type of num. try again"),
                          call([3, 7]),
                          call('for not even value must be >=7, for even >=4'),
                          call([3, 17]),
                          call("for not even value must be >=7, for even >=4"),
                          call("for not even value must be >=7, for even >=4"),
                          call([3, 3]),
                          call('Bye!'),
                          ])



if __name__ == "__main__":
    unittest.main()

