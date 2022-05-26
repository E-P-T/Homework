# The Task 4.5


from typing import Tuple


def option_1(num: int) -> Tuple[int]:
    '''Returns a tuple of a given integer's digits

    Option number 1.
    '''
    return tuple(int(i) for i in str(num))
