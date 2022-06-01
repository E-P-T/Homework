#! /usr/bin/env python
# Implement a decorator `call_once` which runs a function or method once
# and caches the result. All consecutive calls to this function should return
# cached result no matter the arguments.
# >>> python
# @call_once
# def sum_of_numbers(a, b):
#     return a + b
# print(sum_of_numbers(13, 42))
# >>> 55
# print(sum_of_numbers(999, 100))
# >>> 55
# print(sum_of_numbers(134, 412))
# >>> 55
# print(sum_of_numbers(856, 232))
# >>> 55


"""
task_6.py: Implemented a decorator `call_once` which runs a function or method
once and caches the result. All consecutive calls to this function should
return cached result no matter the arguments. Module also contains some tests
for this decorator.
"""


import timeit
from numpy import average as avg


def call_once(func):
    """
    call_once: enclosing function for wrapper which returns wrapper.
    Wrapper gets cache state and can return it for any other calls.
    """
    cache = None

    def wrapper(*args, **kwargs):
        """
        wrapper: calls function and returns cache which is the result of the
        first call.
        """
        nonlocal cache
        if cache is None:
            cache = func(*args, **kwargs)
        return cache

    return wrapper


@call_once
def sum_of_numbers(a, b):
    """
    sum_of_numbers: returns sum of two numbers 'a' and 'b'
    """
    return a + b


def call_once2(func):
    """
    call_once2: enclosing function for wrapper which returns wrapper.
    Wrapper gets cache state and can return it for any other calls.
    """
    def wrapper(*args, **kwargs):
        """
        wrapper: calls function and returns cache which is the result of the
        first call.
        """
        if call_once2.cache is None:
            call_once2.cache = func(*args, **kwargs)
        return call_once2.cache

    call_once2.cache = None

    return wrapper


@call_once2
def sum_of_numbers2(a, b):
    """
    sum_of_numbers2: returns sum of two numbers 'a' and 'b'
    """
    return a + b


cache = None


def call_once3(func):
    """
    call_once3: enclosing function for wrapper which returns wrapper.
    Wrapper gets cache state and can return it for any other calls.
    """

    def wrapper(*args, **kwargs):
        """
        wrapper: calls function and returns cache which is the result of the
        first call.
        """
        global cache
        if cache is None:
            cache = func(*args, **kwargs)
        return cache

    return wrapper


@call_once3
def sum_of_numbers3(a, b):
    """
    sum_of_numbers3: returns sum of two numbers 'a' and 'b'
    """
    return a + b


def caller(func):
    func(13, 42)
    func(999, 100)
    func(134, 412)
    func(856, 232)


if __name__ == "__main__":
    print(sum_of_numbers(13, 42))  # Result: 55
    print(sum_of_numbers(999, 100))  # Result: 55
    print(sum_of_numbers(134, 412))  # Result: 55
    print(sum_of_numbers(856, 232))  # Result: 55

    print(sum_of_numbers2(13, 42))  # Result: 55
    print(sum_of_numbers2(999, 100))  # Result: 55
    print(sum_of_numbers2(134, 412))  # Result: 55
    print(sum_of_numbers2(856, 232))  # Result: 55

    print(sum_of_numbers3(13, 42))  # Result: 55
    print(sum_of_numbers3(999, 100))  # Result: 55
    print(sum_of_numbers3(134, 412))  # Result: 55
    print(sum_of_numbers3(856, 232))  # Result: 55

    result = timeit.repeat(
        stmt="caller(sum_of_numbers)",
        number=10000,
        repeat=10,
        globals=globals()
    )
    print(avg(result))  # Result: 0.004293040799893788

    result = timeit.repeat(
        stmt="caller(sum_of_numbers2)",
        number=10000,
        repeat=10,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0052323628000522145

    result = timeit.repeat(
        stmt="caller(sum_of_numbers3)",
        number=10000,
        repeat=10,
        globals=globals()
    )
    print(avg(result))  # Result: 0.004471497499980615

    # As we can see, nonlocal changes is faster than chaning to function
    # attribute or changing globas variables. Also it's more readable and
    # acceptable way to do this task.
