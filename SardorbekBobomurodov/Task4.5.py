from typing import Tuple


def get_digits(input_num: int) -> Tuple[int]:
    """Returns a tuple of a given integer's digits"""
    return tuple(int(i) for i in str(input_num))


if __name__ == '__main__':
    while True:
        num = input("Input a number: ")
        print(get_digits(num), end="\n")
