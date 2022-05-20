"""
Task 7.5
Implement function for check that number is even, at least 3. Throw different exceptions for this errors.
Custom exceptions must be derived from custom base exception(not Base Exception class).
"""


class CustomException(Exception):
    def __init__(self):
        self.message = "Common exception"

    def __str__(self):
        return f"The function raised an error: {self.message}"


class WrongTypeOfArgument(CustomException):
    def __init__(self):
        self.message = f"The argument must be integer"


class WrongTypeOfArgumentFloat(CustomException):
    def __init__(self):
        self.message = f"The argument cannot be float"


def is_even(number: int):
    try:
        if isinstance(number, int):
            print(f"{number} is even") if number % 2 == 0 else print(f"{number} is odd")
        else:
            if isinstance(number, float):
                raise WrongTypeOfArgumentFloat
            else:
                raise WrongTypeOfArgument
    except CustomException as ex:
        print(ex)


if __name__ == '__main__':
    a = '2'
    b = 6
    c = 0.2
    is_even(a)

