# Task 4.3
# Implement a function which works the same as `str.split` method
# (without using `str.split` itself, ofcourse).


def sep_func(string, sep=' '):
    if sep in string:
        result_list, index = [], 0
        while True:
            i = string.find(sep, index)
            if i == -1:
                result_list.append(string[index:])
                break
            result_list.append(string[index:i])
            index = i + 1
    else:
        return [string]
    return result_list


print(sep_func('12323', '2'))
