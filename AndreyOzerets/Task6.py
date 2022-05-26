# Task 2.6

from typing import Tuple


def with_join(numbers: Tuple[int]) -> int:
    '''Convert a tuple of positive integers to a number

    Implemented via join and generator comprehension.
    '''
    gen_numbers = (str(i) for i in numbers)
    str_number = int(''.join(gen_numbers))
    return str_number
