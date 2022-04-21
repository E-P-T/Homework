# Task 4.1
# Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa.


def replace_quotation(string:str) -> str:
    """
    The function takes a string as an argument and processes it by replacing all symbols that are included into
    replace_dict as keys with their corresponding values, and returns a new string

    :param string: input string
    :return: a resulting string
    :raises AssertionError if input is not string type
    """
    assert isinstance(string, str), 'Incorrect input. Input must be a string'
    replace_dict = {'"': "'", "'": '"'}
    return ''.join([replace_dict[i] if i in replace_dict else i for i in string])


# s = """She's his best friend "WOW" she says"""
# s = ''
# print(replace_quotation(s))
