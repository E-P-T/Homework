import unittest
from unittest.mock import patch
from task7_6 import Solution
from task7_5 import *


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Solution()
    
    def test_is_even(self):
        self.assertTrue(is_even(10))
        self.assertTrue(is_even(4))
        self.assertFalse(is_even("umid"))   
        self.assertFalse(is_even(9))
        self.assertFalse(is_even(1))
    

    def test_is_prime(self):
        self.assertFalse(self.s.is_prime(9))
        self.assertFalse(self.s.is_prime(1))
        self.assertTrue(self.s.is_prime(23))
    
        with self.assertRaises(TypeError):
            self.s.is_prime("u")
    

    def test_find_primes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        self.s.number = 20
        self.assertEqual(self.s.find_primes(), primes)
    
    
    @patch("__main__.Solution.find_primes")
    def test_goldbach_and_primes(self, mocked_method):
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        self.s.number = 20
        mocked_method.return_value = primes

        goldbach_result = self.s.goldbach_conjecture()
        self.assertEqual((3, 17), goldbach_result)
        mocked_method.assert_called_once()
 

if __name__ == "__main__":
    unittest.main()
