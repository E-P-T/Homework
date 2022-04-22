def foo(string):
    C = [",", ".", " ", "?", "!"]
    new_s = ""
    for c in string:
        if c in C:
            continue
        else:
            new_s += c
    reversed = new_s[-1::-1]
    if new_s == reversed:
        return True
    else:
        return False
s = input("string: ").lower()
print(foo(s))


