def call_once(func):
    result = None
    def inner(a, b):
        nonlocal result
        result = a + b if result is None else result
        print(result)
    return inner

@call_once
def sum_of_numbers(a, b):
    return a + b

sum_of_numbers(13, 42)
sum_of_numbers(1, 4)
sum_of_numbers(11, 4)
sum_of_numbers(11, 44)