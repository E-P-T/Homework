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


class NotEvenValue(CustomException):
    def __init__(self):
        self.message = f"The value is odd"


class ValueBelowTwo(CustomException):
    def __init__(self):
        self.message = f"The value lower than 2"