# The Task 4.5


from typing import List, Tuple


def option_1(num: int) -> Tuple[int]:
    '''Returns a tuple of a given integer's digits

    Option number 1.
    '''
    return tuple(int(i) for i in str(num))


def option_2(num: int) -> Tuple[int]:
    '''Returns a tuple of a given integer's digits

    Option number 2.
    '''
    digits: List[int] = []
    digits_append = digits.append
    while num:
        digits_append(num % 10)
        num //= 10
    return tuple(digits[::-1])
