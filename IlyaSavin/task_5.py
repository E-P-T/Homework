#! /usr/bin/env python
# TODO: Implement a decorator `remember_result` which remembers last result
# of function it decorates and prints it before next call.
# >>> python
# @remember_result
# def sum_list(*args):
# 	result = ""
# 	for item in args:
# 		result += item
# 	print(f"Current result = '{result}'")
# 	return result
# sum_list("a", "b")
# >>> "Last result = 'None'"
# >>> "Current result = 'ab'"
# sum_list("abc", "cde")
# >>> "Last result = 'ab'"
# >>> "Current result = 'abccde'"
# sum_list(3, 4, 5)
# >>> "Last result = 'abccde'"
# >>> "Current result = '12'"


"""
task_5.py: implemented decorator "remember_result" which remembers last result
of funtion it decorates and prints it before next call. Also contains some
tests for this decorator.
"""


import timeit
from numpy import average as avg


def remember_result(func):
    """
    remember_result: enclosing function for wrapper which returns wrapper.
    Wrapper gets state of result, so it can change state of result and it will
    be saved. Result is a variable from enclosing function.
    """
    result = None

    def wrapper(*args, trace=False, **kwargs):
        """
        wrapper: calls function and changes the result from enclosing function.
        Also takes flag for printing. If trace is true, it will print output.
        """
        nonlocal result
        if trace:
            print("Last result = '" + str(result) + "'")
        result = func(trace=trace, *args, **kwargs)
        return result

    return wrapper


def remember_result2(func):
    """
    remember_result2: enclosing function for wrapper which returns wrapper.
    Wrapper gets state of result, so it can change state of result and it will
    be saved. Result is an attribute of enclosing function.
    """
    def wrapper(*args, trace=False, **kwargs):
        """
        wrapper: calls function and changes the result from enclosing function.
        Also takes flag for printing. If trace is true, it will print output.
        """
        if trace:
            print("Last result = '" + str(remember_result2.result) + "'")
        remember_result2.result = func(trace=trace, *args, **kwargs)
        return remember_result2.result

    remember_result2.result = None

    return wrapper


result = None


def remember_result3(func):
    """
    remember_result3: enclosing function for wrapper which returns wrapper.
    Wrapper gets state of result, so it can change state of result and it will
    be saved. Result is a global variable.
    """
    def wrapper(*args, trace=False, **kwargs):
        """
        wrapper: calls function and changes the result from global function.
        Also takes flag for printing. If trace is true, it will print output.
        """
        global result
        if trace:
            print("Last result = '" + str(result) + "'")
        result = func(trace=trace, *args, **kwargs)
        return result

    return wrapper


@remember_result
def sum_list(*args, trace=False):
    """
    """
    result = ""
    for item in args:
        result += item
    if trace:
        print(f"Current result = '{result}'")
    return result


@remember_result2
def sum_list2(*args, trace=False):
    """
    sum_list2: concatenates string in one string and returs it.
    """
    result = ""
    for item in args:
        result += item
    if trace:
        print(f"Current result = '{result}'")
    return result


@remember_result3
def sum_list3(*args, trace=False):
    """
    sum_list2: concatenates string in one string and returs it.
    """
    result = ""
    for item in args:
        result += item
    if trace:
        print(f"Current result = '{result}'")
    return result


def caller(func):
    func('a', 'b')
    func("abc", "cde")
    func('3', '4', '5')


if __name__ == "__main__":
    sum_list('a', 'b', trace=True)
    sum_list("abc", "cde", trace=True)
    sum_list('3', '4', '5', trace=True)
    # Result:
    # Last result = 'None'
    # Current result = 'ab'
    # Last result = 'ab'
    # Current result = 'abccde'
    # Last result = 'abccde'
    # Current result = '345'

    sum_list2('a', 'b', trace=True)
    sum_list2("abc", "cde", trace=True)
    sum_list2('3', '4', '5', trace=True)
    # Result:
    # Last result = 'None'
    # Current result = 'ab'
    # Last result = 'ab'
    # Current result = 'abccde'
    # Last result = 'abccde'
    # Current result = '345'

    sum_list3('a', 'b', trace=True)
    sum_list3("abc", "cde", trace=True)
    sum_list3('3', '4', '5', trace=True)
    # Result:
    # Last result = 'None'
    # Current result = 'ab'
    # Last result = 'ab'
    # Current result = 'abccde'
    # Last result = 'abccde'
    # Current result = '345'

    result = timeit.repeat(
        stmt="caller(sum_list)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.001222584400056803

    result = timeit.repeat(
        stmt="caller(sum_list2)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0014054167997528566

    result = timeit.repeat(
        stmt="caller(sum_list3)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0013965529999040883

    # As we can see, nonlocal changes is faster than chaning to function
    # attribute or changing globas variables. Also it's more readable and
    # acceptable way to do this task.
