# Task 5.2

from typing import List, Optional


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
