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
