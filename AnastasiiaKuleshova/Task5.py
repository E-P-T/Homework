# Task 5.5
# Implement a decorator remember_result which remembers last result
# of function it decorates and prints it before next call.
#

#
# sum_list("a", "b")
# >>> "Last result = 'None'"
# >>> "Current result = 'ab'"
# sum_list("abc", "cde")
# >>> "Last result = 'ab'"
# >>> "Current result = 'abccde'"
# sum_list(3, 4, 5)
# >>> "Last result = 'abccde'"
# >>> "Current result = '12'"

# @remember_result
# def sum_list(*args):
# 	result = ""
# 	for item in args:
# 		result += item
# 	print(f"Current result = '{result}'")
# 	return result
previous_result = None


def remember_result(func):
    def wrapper(*args, **kwargs):
        global previous_result
        print(f"Last result={previous_result}")
        previous_result = func(*args, **kwargs)
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


sum_list('2','3')
sum_list('3','4')
