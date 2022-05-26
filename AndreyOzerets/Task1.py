# The Task 4.1

from typing import Iterable


def get_char(str_: str, ch1: str, ch2: str) -> Iterable[str]:
    '''Return each character of a string

    At the same time, it replaces the characters of the string ch1 with ch2.
    '''
    for i in str_:
        if i == ch1:
            i = ch2
        elif i == ch2:
            i = ch1
        yield i
