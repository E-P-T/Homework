# Task 4.5
# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
# of a given integer's digits.
# Example:
# ```python
# >>> split_by_index(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
# ```


def get_digits(num: int) -> tuple:
    digits = list()
    sign = 1
    if num == 0:
        digits.append(0)
    if num < 0:
        num = - num
        sign = -1
    while num > 0:
        digits.append(num % 10)
        num = num // 10
    if sign == -1:
        digits.append('-')
    digits.reverse()
    return tuple(digits)
