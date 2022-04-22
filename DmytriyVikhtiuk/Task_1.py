def foo(string):
    D = "\""
    O = "\'"
    new_s =""
    for c in string:
        if c == "\"":
            c = O
        elif c =="\'":
            c = D
        new_s += c
    return new_s

s = input("type your string: ")
print(foo(s))