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


def strip_chars(words: List[str], chars: str = ' ') -> List[str]:
    '''Return strings with the leading and trailing characters removed.'''
    clean_words: List[str] = []
    clean_words_append = clean_words.append
    for i in words:
        clean_words_append(i.strip(chars))
    return clean_words
