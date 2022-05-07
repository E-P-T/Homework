"""
Task 5.5
Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call
"""

from decorators import remember_result


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    return result


sum_list("a", "b")
sum_list(3, 4, 5)
sum_list("abc", "cde")
