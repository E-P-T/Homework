'''
Task 4.1
Implement a function which receives a string and replaces all `"` symbols
with `'` and vise versa.
'''


def replace_string(string: str) -> str:
    list_of_symbols = []
    for s in string:
        if s == '"':
            list_of_symbols.append("'")
        elif s == "'":
            list_of_symbols.append('"')
        else:
            list_of_symbols.append(s)
    return ''.join(list_of_symbols)


print(replace_string("'Python'"))
