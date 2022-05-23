import unittest
from goldbachprogram import MyException, isEven, EmptyException, StringException, BoolException, TypeException, isPrime, primesList, goldbach

class TestGoldbach(unittest.TestCase):

    def test_MyException(self):
        self.assertEqual(str(MyException('message')), 'message')
        self.assertEqual(str(MyException()), '')                                
        self.assertEqual(str(MyException('True')), 'True')
        self.assertEqual(str(MyException('word')), 'word')

    def test_isEven(self):
        self.assertTrue(isEven(0))
        self.assertTrue(isEven(24))
        self.assertTrue(isEven(-24))
        self.assertFalse(isEven(17))
        self.assertFalse(isEven(-17))
        with self.assertRaises(EmptyException):
            isEven()
        with self.assertRaises(StringException):
            isEven('word')
        with self.assertRaises(BoolException):
            isEven(True)
        with self.assertRaises(TypeException):
            isEven({'a': 1})
        with self.assertRaises(TypeException):
            isEven([])

    def test_isPrime(self):
        with self.assertRaises(EmptyException):
            isPrime()
        with self.assertRaises(TypeException):
            isPrime('word')
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(113))
        self.assertFalse(isPrime(-1))
        self.assertFalse(isPrime(8))
        
    def test_primesList(self):
        with self.assertRaises(EmptyException):
            primesList()
        with self.assertRaises(TypeException):
            primesList('word')
        self.assertEqual(primesList(10), [2,3,5,7])
        self.assertEqual(primesList(4), [2,3])
        self.assertEqual(primesList(60), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59])

    def test_goldbach(self):
        self.assertEqual(goldbach(10), [10, [3, 7]])
        self.assertEqual(goldbach(4), [4, [2, 2]])
        self.assertEqual(goldbach(1000), [1000, [3, 997]])
        with self.assertRaises(MyException):
            goldbach(0)
        with self.assertRaises(MyException):
            goldbach(-1000)
        with self.assertRaises(MyException):
            goldbach(17)

unittest.main()
