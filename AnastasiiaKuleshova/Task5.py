# Task 7.5
# Implement a function for check that number is even, at least 3.
# Throw different exceptions for these errors. Custom exceptions must be derived
# from custom base exception(not Base Exception class).

class MathModuleException(BaseException):
    def __init__(self, message=""):
        self.message = message

    def __str__(self):
        return self.message


class EmptyValue(MathModuleException):
    pass


class WrongType(MathModuleException):
    pass


class Task5:
    def is_even(num):
        try:
            if num is None:
                raise EmptyValue("empty value")
            elif not isinstance(num, int):
                raise WrongType("wrong type")
        except MathModuleException as e:
            print(e)
        else:
            if num % 2 == 0:
                print("number is even")
                return True
            else:
                print("number is not even")
                return False



