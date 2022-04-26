'''Task 4.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa.'''


def replace_symbols(s):
    s = s.translate({ord("'"): '"', ord('"'): "'"})
    return s


def replace_quotes(s):
    res = ""
    table = {"'": "\"", "\"": "'"}
    for i in s:
        if i in table.keys():
            res += table[i]
        else:
            res += i
    return res


print(replace_symbols("'''\"\"\""))
print(replace_quotes("'''\"\"\""))
