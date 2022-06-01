# Task 5.5
# Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.

# ```python
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
# ```

def remember_result(handler):
    """
    Decorator which remembers last result of function it decorates and prints it before next call.
    """
    last_result = None

    def wrapper(*args):
        nonlocal last_result
        print(f"Last result = '{last_result}'")
        last_result = handler(*args)

    return wrapper


@remember_result
def sum_list(*args):
    # Check input types
    result = "" if all([isinstance(item, str) for item in args]) else 0

    for item in args:
        result += item
    print(f"Current result = '{result}'")

    return result


def main():
    """
    Entry point function.
    """
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)


if __name__ == '__main__':
    main()
