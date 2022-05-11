# Task 7.5
# Implement function for check that number is even, at least 3. Throw different exceptions for these errors.
# Custom exceptions must be derived from custom base exception(not Base Exception class).
class CustomException(BaseException):

    def __init__(self, error_message=''):
        self.message = error_message

    def __str__(self):
        return self.message


class TypeException(CustomException):
    pass


class EmptyException(CustomException):
    pass


class BoolException(CustomException):
    pass


class StringException(CustomException):
    pass


def is_even(num: int = None) -> bool:
    if num is None:
        raise EmptyException("Function requires directly one integer argument")
    elif isinstance(num, str):
        raise StringException("Got a string as argument, argument must be an integer")
    elif isinstance(num, bool):
        raise BoolException("Got a Boolean as argument, argument must be an integer")
    elif not isinstance(num, int):
        raise TypeException("Wrong argument type, must be an integer")

    return num % 2 == 0


def main():
    print(is_even(3))
    print(is_even(2))
    try:
        print(is_even())
    except EmptyException as message:
        print(f'Error ocured during function runtime: {message}')
    try:
        print(is_even('2'))
    except StringException as message:
        print(f'Error ocured during function runtime: {message}')
    try:
        print(is_even(True))
    except BoolException as message:
        print(f'Error ocured during function runtime: {message}')
    try:
        print(is_even({5}))
    except TypeException as message:
        print(f'Error ocured during function runtime: {message}')


if __name__ == '__main__':
    main()
