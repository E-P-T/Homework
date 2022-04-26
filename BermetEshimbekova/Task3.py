# Task 4.3
# Implement a function which works the same as `str.split` method
# (without using `str.split` itself, ofcourse).

def same_as_split(text, sep=' '):
    s = ''
    result = []
    for i in text:
        if i == sep:
            if s: result.append(s)
            s = ''
            continue
        s += i
    if s: result.append(s)
    return result


text = "Implement a function    which works the same as `str.split` method (without   using `str.split` itself, ofcourse)"
print(same_as_split(text) == (text.split()))
print(same_as_split(text, 't') == (text.split('t')))