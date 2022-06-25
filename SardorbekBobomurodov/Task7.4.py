import logging
from contextlib import ContextDecorator

logging.basicConfig(level=logging.INFO)


# Method 1
def exception_handler(func):
    def inner_func(*args):
        try:
            func(*args)
        except ZeroDivisionError as error:
            print(error)
        else:
            logging.info("First and Second arguments are: {a} and {b}".format(a=args[0], b=args[1]))

    return inner_func


@exception_handler
def test_func(*random_list):
    print(random_list[0] // random_list[1])


# Method 2
class ExceptionSupress(ContextDecorator):

    def __init__(self, *exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exception:
            print(exc_val)
            return True
        elif exc_type is None:
            logging.info("Success!")


@ExceptionSupress(ZeroDivisionError)
def test_func2(*random_list):
    print(random_list[0] // random_list[1])


if __name__ == "__main__":
    test_func(1, 0)
    test_func(4, 2)
    print("\n")
    test_func2(1, 0)
    test_func2(4, 2)
