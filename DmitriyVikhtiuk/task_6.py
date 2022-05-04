def call_once(func):
    result = 0
    def wrapper(a, b):
        nonlocal result
        if result == 0:
            result = func(a, b)
        else:
            pass
        return result
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(900, 422))
print(sum_of_numbers(143, 42))
print(sum_of_numbers(1, 42))