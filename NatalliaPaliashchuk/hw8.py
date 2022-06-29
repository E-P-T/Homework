import unittest
from unittest.mock import patch

class Error(Exception): pass
   
class ArgError(Error): pass

def iseven(num):
    try:
        if num % 2 == 0:
            return True
        else:
            return False
    except Exception:
        raise ArgError('Bad arg')

    
def goldbach_conjecture():
    while True:
        ent = input()
        if 'q'== ent: break
        try:
            ent = int(ent)
        except ValueError:
            print('Enter the correct even number')
            continue
        if not iseven(ent) or ent < 4:
            print('Enter the correct even number')
            continue
        prime = []
        for i in range(2, ent):
            cnt = 0
            for j in range(2, i + 1):
                if i % j == 0:
                    cnt += 1
            if cnt == 1:
                prime.append(i)
        for i, val in enumerate(prime):
            for j in prime[i:]:
                if val + j == ent:
                    print(val, j)

class TestGoldbachsConjecture(unittest.TestCase):
    def test_iseven(self):
        self.assertTrue(iseven(2))
        self.assertFalse(iseven(1))
        with self.assertRaises(ArgError):
            iseven('')
    
    @patch('input()', return_value='4')
    def test_goldbach_conjecture(self):
        self.assertEqual(goldbach_conjecture(), '2 2')
        


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)