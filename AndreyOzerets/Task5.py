# Task 7.5


class MyBaseError(Exception):

    def __init__(self, number, message):
        super().__init__(number, message)
        self._number = number
        self._message = message
