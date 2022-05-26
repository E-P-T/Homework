# Task 2.6

from typing import Tuple


def with_join(numbers: Tuple[int]) -> int:
    '''Convert a tuple of positive integers to a number

    Implemented via join and generator comprehension.
    '''
    gen_numbers = (str(i) for i in numbers)
    str_number = int(''.join(gen_numbers))
    return str_number


def with_concat(numbers: Tuple[int]) -> int:
    '''Convert a tuple of positive integers to a number

    Implemented via concatenation.
    '''
    str_out = ""
    for i in numbers:
        str_out = str_out + str(i)
    out_int = int(str_out)
    return out_int


def with_map(numbers: Tuple[int]) -> int:
    '''Convert a tuple of positive integers to a number

    Implemented via join and map.
    '''
    return int(''.join(map(str, numbers)))
