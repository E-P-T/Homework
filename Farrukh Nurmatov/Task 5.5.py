"""Implement a decorator `remember_result` which remembers last result
of function it decorates and prints it before next call."""

def remember_result(func):

    last_result = None
    def inner(*args):
        nonlocal last_result
        print(f"Last result = '{last_result}'")
        last_result = func(*args)
    return inner



@remember_result
def sum_list(*args):
    try:
        if args[0].isalpha():
            result = ""
    except AttributeError:
        result = 0
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


if __name__ == '__main__':
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)
