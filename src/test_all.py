import unittest
from pathlib import Path

if __name__ == '__main__':
    path = Path(__file__).parent.joinpath('test')
    tests = unittest.TestLoader().discover(path)
    unittest.TextTestRunner().run(tests)


