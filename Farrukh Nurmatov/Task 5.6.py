"""Implement a decorator `call_once` which runs a function or method once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments."""


def call_once(func):
    cache = None
    def decor(*args):
        nonlocal cache
        if cache is None:
            one = func(*args)
            cache = one
        return cache
    return decor


@call_once
def sum_of_numbers(a, b):
    return a + b

if __name__ == '__main__':
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))