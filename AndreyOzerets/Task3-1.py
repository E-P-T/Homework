# Task 2.3-1

from typing import List


def get_words(greeting: str) -> str:
    '''Return the entered string.'''
    seq = input(greeting)
    return seq


def break_into_words(raw_str: str, sep: str = ',') -> List[str]:
    '''Split string at separator.'''
    words = raw_str.split(sep)
    return words
