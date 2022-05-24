import unittest
from unittest.mock import patch, call
import Task_7_6


class TestEnd2End(unittest.TestCase):
    @patch("builtins.print")
    @patch("Task_7_6.program")
    def test_end_2_end(self, mock_input, mock_print):
        in_out = {"a": "Occurred: This is not number, it is characters!! You are doing something wrong!",
                  "2": "Your number is a sum of 1 and 1",
                  "5": "You should enter even number!",
                  "16": "Your number is a sum of 3 and 13",
                  "1.23": "Occurred: This is not integer number!! You are doing something wrong!",
                  "20": "Your number is a sum of 1 and 19",
                  "96": "Your number is a sum of 7 and 89",
                  "q": "Good buy!"}
        outputs = [call(v) for v in in_out.values()]
        mock_input.side_effect = in_out.keys()
        Task_7_6.program()
        self.assertEqual(mock_print.mock_calls, outputs)


if __name__ == '__main__':
    unittest.main()



