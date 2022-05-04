def remember_result(func):
    last = "None"

    def wrapper(*args):
        nonlocal last
        print(f"Last result = {last}")
        last = func(*args)
        return last

    return wrapper


@remember_result
def sum_list(*args):
    for item in args:
        if type(item) == str:
            result = ""
        else:
            result = 0
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


sum_list("a", "b")
sum_list("abc", "bcd")
sum_list("a1", "b2")
sum_list(1, 2)
sum_list(1.5, 2.7)
