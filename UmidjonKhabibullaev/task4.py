from contextlib import contextmanager
import logging


def ignore_exceptions(f):
    def wrapper(*args, **kwargs):
        try:
            res = f(*args, **kwargs)
            logging.info("No exception has occurred!")
            return res
        except:
            logging.error("Exception suppresed!")
        
    return wrapper



@ignore_exceptions
def division(x, y):
    return x / y


print(division(9, 0))
