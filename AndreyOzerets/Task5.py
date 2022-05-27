# Task 5.5

from functools import wraps


def remember_result(func):
    '''Decorator remembering the last result

    Prints the last result before the next function call
    '''

    last_result = None

    @ wraps(func)
    def wrap(*args):
        nonlocal last_result
        print(f"Last result = {last_result}")

        if all([isinstance(i, int) or isinstance(i, float) for i in args]):
            res = 0
            for i in args:
                res += i
            args = str(res)
            last_result = args
        else:
            args = [str(i) for i in args]
        last_result = func(*args)
    return wrap


@ remember_result
def sum_list(*args):
    '''Concatenate received elements

    Strings are concatenated, numbers are added together.
    '''

    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result
