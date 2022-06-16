# ### Task 5.5
# Implement a decorator `remember_result` which remembers last result of function
# it decorates and prints it before next call.
#
# @remember_result
# def sum_list(*args):
# 	result = ""
# 	for item in args:
# 		result += item
# 	print(f"Current result = '{result}'")
# 	return result
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

def remember_result(func):
    with open('data/remember_result.txt', "r") as file:
        try:
            last_result = file.readlines()
        except:
            last_result = []

    def inner(*args, **kwargs):
        if not last_result:
            print("Last result = 'None'")
        if last_result:
            print(f"Last result =  '{last_result[-1][:-1:]}'")

        with open('data/remember_result.txt', 'a') as file:
            file.write(func(*args, **kwargs) + "\n")

        print(f"Current result = '{func(*args, **kwargs)}'")

        return func(*args, **kwargs)

    return inner


@remember_result
def sum_list(*args):
    if type(list(args)[0]) == str:
        result = ""
    elif type(list(args)[0]) == int:
        result = 0
    for item in args:
        result += item
    return str(result)


# sum_list("a", "b")
# sum_list("abc", "cde")
sum_list(3, 4, 5)