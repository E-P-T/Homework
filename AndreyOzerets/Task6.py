# Task 5.6

from functools import wraps


def call_once(func):
    '''Decorator for caching the first result of a function'''

    cached_result = None

    @wraps(func)
    def wrap(*args, **kwargs):
        nonlocal cached_result
        if cached_result is None:
            cached_result = func(*args, **kwargs)
        return cached_result
    return wrap


@call_once
def sum_of_numbers(a, b):
    '''Return the sum of two numbers'''

    return a + b
