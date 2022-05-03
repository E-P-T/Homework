# Task 5.6
# Implement a decorator call_once which runs a function or method
# once and caches the result. All consecutive calls to this function
# should return cached result no matter the arguments.
#
# @call_once
# def sum_of_numbers(a, b):
#     return a + b
#
# print(sum_of_numbers(13, 42))
# >>> 55
# print(sum_of_numbers(999, 100))
# >>> 55
# print(sum_of_numbers(134, 412))
# >>> 55
# print(sum_of_numbers(856, 232))
# >>> 55
cache = None


def call_once(func):
    def wrapper(*args, **kwargs):
        global cache
        if cache is None:
            cache = func(*args, **kwargs)
        return cache
    return wrapper



@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(2, 4))
print(sum_of_numbers(5, 6))
print(sum_of_numbers(5, 600))
