import unittest
from unittest.mock import MagicMock, call

from AnastasiiaKuleshova.Task7_6 import Goldbach, Math_Utils
import sys


class GoldbachTest(unittest.TestCase):
    def test_goldbach_success(self):
        Math_Utils.is_prime = MagicMock()
        Math_Utils.is_prime.side_effect = [True, False, True, True]
        actual_result = Goldbach.goldbach_resolve(50)
        calls = [call(2), call(48), call(3), call(47)]
        Math_Utils.is_prime.assert_has_calls(calls)
        expected_result = (3, 47)
        self.assertEquals(actual_result, expected_result)

    def test_goldbach_input_str_sould_throw_exeption(self):
        with self.assertRaises(TypeError):
            Goldbach.goldbach_resolve("fjfj")

    def test_is_prime_input_is_prime(self):
        actual_result = Math_Utils.is_prime(7)
        self.assertTrue(actual_result)

    def test_is_prime_input_is_positive_not_prime(self):
        actual_result = Math_Utils.is_prime(8)
        self.assertFalse(actual_result)

    def test_is_prime_input_is_zero(self):
        actual_result = Math_Utils.is_prime(0)
        self.assertFalse(actual_result)

    def test_is_prime_input_is_negative_prime(self):
        actual_result = Math_Utils.is_prime(-13)
        self.assertTrue(actual_result)

    def test_is_prime_input_is_negative_not_prime(self):
        actual_result = Math_Utils.is_prime(-12)
        self.assertFalse(actual_result)

    def test_is_prime_input_is_edge_positive_prime(self):
        actual_result=Math_Utils.is_prime(sys.maxsize)
        self.assertFalse(actual_result)

    def test_is_prime_input_is_literal_should_trow_exept(self):
        with self.assertRaises(TypeError):
            Math_Utils.is_prime("asc")

