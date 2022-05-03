"""Implement a decorator `call_once` which runs a function or method once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.
"""

def call_once(f):
    res = None
    def wrapper(*args):
        nonlocal res
        if res == None:
            res = f(*args)
        return res
    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))

print(sum_of_numbers(999, 100))

print(sum_of_numbers(134, 412))

print(sum_of_numbers(856, 232))