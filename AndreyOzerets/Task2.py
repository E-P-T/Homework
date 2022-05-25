# Task 2.2

from collections import Counter
from typing import Dict


def get_str(greeting: str) -> str:
    '''Return the entered string.'''
    seq = input(greeting)
    return seq


def get_lower_str(string: str) -> str:
    '''Return lowercase string.'''
    return string.lower()


def count(string: str) -> Dict[str, int]:
    '''Return a dictionary with the number of characters in a string.'''
    return dict(Counter(string))


if __name__ == '__main__':
    print()
    print('{:*^30}'.format('The task 2.2'), end='\n\n')
    str_ = get_str('Enter string: ')
    print(f'Result: {count(get_lower_str(str_))}')
