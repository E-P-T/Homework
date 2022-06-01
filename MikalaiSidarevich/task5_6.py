# Task 5.6
# Implement a decorator `call_once` which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.

# ```python
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
# ```

def call_once(handler):
    """
    Decorator which caches result of function it decorates.
    """
    cache = None

    def wrapper(*args):
        nonlocal cache
        if cache is None:
            cache = handler(*args)

        return cache

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


def main():
    """
    Entry point function.
    """
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))


if __name__ == '__main__':
    main()
