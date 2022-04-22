"""Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
of a given integer's digits."""


def get_digits(num: int):
    nums = [int(i) for i in str(num)]
    return tuple(nums)


if __name__ == '__main__':
    print(get_digits(87178291199))