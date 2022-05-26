# Task 5.2

from collections import Counter
from typing import Callable, List, Optional


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
