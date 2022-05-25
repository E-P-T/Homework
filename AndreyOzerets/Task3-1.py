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


def sort_seq(data: List[str], **kwargs) -> List[str]:
    '''Return a new sorted list.'''
    return sorted(set(data), **kwargs)


if __name__ == '__main__':
    print()
    print('{:*^30}'.format('The task 2.3-1'), end='\n\n')
    raw_data = get_words('Enter words separated by commas: ')
    words = break_into_words(raw_data)
    clean_words = strip_chars(words)
    output = sort_seq(clean_words)
    print(output)
