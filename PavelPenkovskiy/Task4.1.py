# Task 4.1
# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa


def replace_symbols(string):
    result = ''
    for i in string:
        if i == '"':
            result += "'"
        elif i == "'":
            result += '"'
        else:
            result += i
    return result


print(replace_symbols(""" "''dfsddfgdg"'212f' """))

