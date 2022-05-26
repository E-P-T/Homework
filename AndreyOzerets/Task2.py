# Task 5.2

from collections import Counter
from functools import partial
from os import path
from string import punctuation
from typing import Callable, List, Optional, Tuple


def words(string_: str,
          punct: str,
          empty_line: str = '\n',
          **kwargs) -> Optional[List[str]]:
    '''Return a word list of a string'''

    if not string_ == empty_line:
        raw_words = string_.lower().split(**kwargs)
        words = [i.strip(punct) for i in raw_words]
        return words
    else:
        return None


def result(list_result: List[Tuple[str, int]]) -> List[str]:
    '''Create a word list'''

    result = [i[0] for i in list_result]
    return result


def most_common_words(filepath: str,
                      get_words: Callable[..., Optional[List[str]]],
                      number_of_words: int = 3,
                      **kwargs) -> List[str]:
    '''Get a list of the most popular words'''

    out: Counter = Counter()
    with open(filepath, **kwargs) as file:
        for i in file:
            words_list = get_words(i)
            if words_list:
                c = Counter(words_list)
                out += c

    return result(out.most_common(number_of_words))


if __name__ == '__main__':

    filepath = 'data/lorem_ipsum.txt'

    if path.exists(filepath):
        get_words = partial(words, punct=punctuation)
        words_list = most_common_words(filepath, get_words)
        print()
        print('{:*^30}'.format('Task 5.2'), end='\n\n')
        print(f'The most used words in the file: {words_list}', end='\n\n')
    else:
        print(f'File "{filepath}" does not exist', end='\n\n')
