#  Task 4.9

from functools import reduce
from string import ascii_lowercase


def test_1_1(*args):
    '''Return characters that occur in all strings'''

    return reduce(lambda a, b: a & b, map(set, args))


def test_1_2(*args):
    '''Return characters that occur in at least one string'''

    return reduce(lambda a, b: a | b, map(set, args))


def test_1_3(*args):
    '''Return characters that occur in at least two strings'''

    res = set()

    for i in args:
        for j in args:
            if i != j:
                res |= set(i) & set(j)
    return res


def test_1_4(*args):
    '''Return characters that are not used in any string'''
    return set(ascii_lowercase)-test_1_2(*args)
