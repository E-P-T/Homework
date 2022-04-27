# Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given integer's digits.
# Example:
#
# >>> split_by_index(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)

def get_digits(num: int) -> [int]:
    # return tuple([int(dig) for dig in num])
    result_list = []
    num = str(num)
    for index in range(0, len(num)):
        result_list.append(int(num[index]))
    result_tuple = tuple(result_list)
    return result_tuple


print(get_digits("247474"))
