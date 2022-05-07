"""
This file allows me to have some practice with decorators (just to make it fun)
"""


def converter(function):
    def wrapper(*args):
        converted_dict = function(*args)
        for item in converted_dict:
            for key, value in item.items():
                if key == 'age':
                    item[key] = int(value)
                elif key == 'average mark':
                    item[key] = float(value)
        return converted_dict
    return wrapper


def remember_result(func):
    previous_results = []

    def wrapper(*args, **kwargs):
        if previous_results:
            print('Last result: ', previous_results[-1])
        else:
            print('Last result: ', None)
        result = func(*args, **kwargs)
        previous_results.append(result)
        print("Current result: ", result)
        return result
    return wrapper


def call_once(func):
    results = []

    def wrapper(*args, **kwargs):
        results.append(func(*args, **kwargs))
        return results[0]
    return wrapper
