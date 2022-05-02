"""Task 4.5
Implement a decorator remember_result which remembers last result of function it decorates
and prints it before next call.
"""
def remember_result(f):
    last_call = None

    def inner_function(*args):
        nonlocal last_call
        print(last_call)
        last_call = f(*args)
    return inner_function
@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result

sum_list("a", "b")