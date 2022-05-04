# ### Task 4.3
# Implement a function which works the same as `str.split` method
# (without using `str.split` itself, ofcourse).


def ft_split(string, delim=' ', max_c=-1):
    ret = []
    word = ""
    if max_c == -1:
        max_c = len(string)
    if max_c < -1:
        max_c = 0
    for c in string:
        if c != delim:
            word += c
        elif c == delim:
            if max_c > 0:
                ret.append(word)
                max_c -= 1
                word = ""
            else:
                word += c
    ret.append(word)

    return ret