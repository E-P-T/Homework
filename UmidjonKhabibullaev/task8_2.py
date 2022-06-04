import unittest
from unittest.mock import patch
from task7_6 import Solution


class GoldbachEnd2EndTest(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        """ Set Up a Solution object for the whole Test.
        """
        self.s = Solution()
    
    @patch("task7_6.input") # replace the input function for providing inputs with side effect
    @patch("task7_5.print") # replace the print of `task7_5` module to see whether `is_even` is printing the right things
    def testSolutionClass(self, mocked_print, mocked_input):
        """ Tests for Solution class for handling possible cases with all of its methods and attrs
        """
        expected_inputs = ["umid", [10, 11, 12], "10", "9", "2"] # provide test inputs to give them to `s.get_input()`
        expected_outputs = [False, False, "10", False, False]    # the expected outputs of `s.get_input()` when receiving inputs above
        # expected prints of `is_even` when called from `s.get_input()` with `expected_inputs`
        expected_prints = ["Error: The provided number is not even", "Error: The provided number is not greater than three"]
        mocked_input.side_effect = expected_inputs
        i = 0 # iterator of mocked print calls

        for output in expected_outputs:
            self.assertEqual(self.s.get_input(), output)
            if output in expected_inputs[-2:]:
                mocked_print.assert_called_with(expected_prints[i])
                i += 1
        
        gc = self.s.goldbach_conjecture() # save the result to test for different cases

        self.assertIsInstance(gc, tuple)
        self.assertEqual(sum(gc), self.s.number)
        for number in gc:
            self.assertTrue(self.s.is_prime(number))
        self.assertEqual(gc, (3, 7))
        

if __name__ == "__main__":
    unittest.main()
