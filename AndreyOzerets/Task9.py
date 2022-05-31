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


if __name__ == '__main__':

    test_strings = ["hello", "world", "python", ]
    print()
    print('{:*^30}'.format('Task 4.9'), end='\n\n')

    print(f'Task 4.9-1: {test_1_1(*test_strings)}', end='\n\n')
    print(f'Task 4.9-2: {test_1_2(*test_strings)}', end='\n\n')
    print(f'Task 4.9-3: {test_1_3(*test_strings)}', end='\n\n')
    print(f'Task 4.9-4: {test_1_4(*test_strings)}', end='\n\n')
