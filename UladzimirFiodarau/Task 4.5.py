# Task 4.5
# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
# of a given integer's digits.


def get_digits(num: int) -> tuple[int]:
    """
    The function takes an integer as an argument and returns a tuple of its digits
    :param num: taken integer
    :return: tuple of integer's digits
    :raises AssertionError if argument is not an integer
    """
    assert isinstance(num, int), "Incorrect input. Input must be an integer"
    return tuple(int(i) for i in str(num))

print(get_digits(87178291199))
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)

print(get_digits(2.5))
# AssertionError: Incorrect input. Input must be an integer