# Task 5.6
# Implement a decorator `call_once` which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.

# ```python
# @call_once
# def sum_of_numbers(a, b):
#    return a + b

# print(sum_of_numbers(13, 42))
# >>> 55
# print(sum_of_numbers(999, 100))
# >>> 55
# print(sum_of_numbers(134, 412))
# >>> 55
# print(sum_of_numbers(856, 232))
# >>> 55
# ```

def call_once(func):
    with open('data/cache_result.txt', "r") as file:
        try:
            cache_result = file.readline()
        except:
            cache_result = None

    def inner(*args, **kwargs):
        with open('data/cache_result.txt', 'a') as file:
            if not cache_result:
                file.write(func(*args, **kwargs))

        if cache_result:
            return cache_result
        else:
            return func(*args, **kwargs)

    return inner


@call_once
def sum_of_numbers(a, b):
    return str(a + b)


# print(sum_of_numbers(13, 42))
# print(sum_of_numbers(999, 100))
# print(sum_of_numbers(134, 412))
print(sum_of_numbers(856, 232))
