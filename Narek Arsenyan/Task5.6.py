def callOnce(func):
    a = None
    def inner(*args):
        nonlocal a
        if a == None:
            a=func(*args)
            return a
        else:
            return a
    return inner

@callOnce
def sum_of_numbers(a, b):
    return a + b
print(sum_of_numbers(2,3))
print(sum_of_numbers(3,4))
print(sum_of_numbers(5,6))
print(sum_of_numbers(7,8))
