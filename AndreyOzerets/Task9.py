#  Task 4.9

from functools import reduce


def test_1_1(*args):
    '''Return characters that occur in all strings'''

    return reduce(lambda a, b: a & b, map(set, args))
