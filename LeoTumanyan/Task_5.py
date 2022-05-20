# ### Task 7.5
# TODO: Implement function for check that number is even, at least 3. Throw different exceptions for this errors.
#  Custom exceptions must be derived from custom base exception(not Base Exception class).

class MyError(Exception):
    def __init__(self):
        self.message = ''

    def __str__(self):
        return f'Error: {self.message}'


class LessThenError(MyError):
    def __init__(self, value):
        self.message = f"{value} is too small"


class EvenError(MyError):
    def __init__(self, value):
        self.message = f"{value} is even"


class WrongType(MyError):
    def __init__(self, value):
        self.message = f"The argument should be integer not {type(value)}"


class WrongArgs(MyError):
    def __init__(self):
        self.message = "You must give one argument."


def is_odd(*args):
    try:
        if len(args) != 1:
            raise WrongArgs
        if not isinstance(args[0], int):
            raise WrongType(args[0])
        if args[0] < 3:
            raise LessThenError(args[0])
        if not args[0] % 2:
            raise EvenError(args[0])
    except MyError as e:
        print(e)
        return False
    else:
        print(f'{args[0]} is odd')
        return True


def is_even(*args):
    try:
        if len(args) != 1:
            raise WrongArgs
        if not isinstance(args[0], int):
            raise WrongType(args[0])
        if args[0] < 3:
            raise LessThenError(args[0])
        if args[0] % 2:
            raise EvenError(args[0])
    except MyError as e:
        print(e)
    else:
        return True


# is_odd(8)
# is_odd('othello')
# is_odd(8.9)
# is_odd(8, 9, 45)
# is_odd()
# is_odd(-7)
# is_odd(13)
