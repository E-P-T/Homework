# Task 4.1
# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa.


def repl_func(string):
    if "'" in string:
        string = string.replace("'", '"')
    else:
        string = string.replace('"', "'")
    return string
