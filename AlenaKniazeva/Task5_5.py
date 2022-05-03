"""Implement a decorator `remember_result` which remembers last result of function
it decorates and prints it before next call.
"""

def remember_result(f):
    last_res = None
    def wrapper(*args):
        nonlocal last_res
        print(f"Last result = '{last_res}'")
        last_res = f(*args)
        return last_res
    return wrapper

@remember_result
def sum_list(*args):
	result = args[0]
	for item in args[1:]:
		result += item
	print(f"Current result = '{result}'")
	return result

sum_list("a", "b")

sum_list("abc", "cde")

sum_list(3, 4, 5)