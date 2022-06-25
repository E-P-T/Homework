class CustomException(Exception):
    pass


class StringException(CustomException):
    pass


class NotIntegerException(CustomException):
    pass


def is_even(number):
    if isinstance(number, str):
        raise StringException("Number is string!")
    elif not isinstance(number, int):
        raise NotIntegerException("Number is not integer!")
    return number % 2 == 0


if __name__ == "__main__":
    print(is_even(4))
    print(is_even(4.2))
    print(is_even("abs"))
    print(is_even(3))
    print(is_even(43))
    print(is_even(8))
    print(is_even(-8))
