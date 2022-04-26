# Task 4.1

def changequotes(s):
    new_s = []
    for symbol in s:
        if symbol == '\"':
            symbol = '\''
        elif symbol == '\'':
            symbol = '\"'
        new_s.append(symbol)

    return ''.join(new_s)


string = '''Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa.'''
print(changequotes(string))
