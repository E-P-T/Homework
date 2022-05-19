def call_once(f):
    res = None

    def wrapper(*args):
        nonlocal res
        if res == None:
            res = f(*args)
        return res

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


if __name__ == '__main__':
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(0, 42))
    print(sum_of_numbers(13, 1))
