# Task 7.5


class MyBaseError(Exception):
    """Base class for native error"""

    def __init__(self, number, message):
        super().__init__(number, message)
        self._number = number
        self._message = message

    def __str__(self):
        return f'{self._number} - {self._message}'


class WrongTypeError(MyBaseError):
    """Class for type errors"""

    def __init__(self, number, message='is not a number') -> None:
        super().__init__(number, message)


class NegativeError(MyBaseError):
    """Class of positive errors"""

    def __init__(self, number, message='must be positive'):
        super().__init__(number, message)


def check_parity(number: int) -> bool:

    if not isinstance(number, int):
        raise WrongTypeError(number)

    if number is False:
        raise MyBaseError(number, 'cannot be False')

    if number < 0:
        raise NegativeError(number)

    return number % 2 == 0


if __name__ == '__main__':
    try:
        print(check_parity(-9))
    except WrongTypeError as e:
        print(e)
    except MyBaseError as e:
        print(e)
    except NegativeError as e:
        print(e)
    else:
        print('OK')
