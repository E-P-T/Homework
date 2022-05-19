def remember_result(f):
    prev = None

    def wrapper(*args):
        nonlocal prev
        print(prev)
        prev = f'Previous result {f(*args)}'
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


if __name__ == '__main__':
    sum_list('a', 'b')
    sum_list('c', 'd')
    sum_list('e', 'f')
