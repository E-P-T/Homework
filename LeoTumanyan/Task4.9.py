# ### Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
#
# 1) characters that appear in all strings
def test_1(*strings: str):
    return set.intersection(*map(set, strings))
    # prim = [0] * 255
    # ret = set()
    # for s in strings[0]:
    #     for string in strings:
    #         if s in string:
    #             prim[ord(s)] += 1
    # for i in range(255):
    #     if prim[i] == len(strings):
    #         ret.add(chr(i))
    # return ret


# 2) characters that appear in at least one string
def test_2(*strings: str):
    return set.union(*map(set, strings))

# 3) characters that appear at least in two strings


def test_3(*strings: str):
    prim = [0] * 255
    ret = set()
    for s in strings[0]:
        for string in strings:
            if s in string:
                prim[ord(s)] += 1
    for i in range(255):
        if prim[i] > 1:
            ret.add(chr(i))
    return ret


# 4) characters of alphabet, that were not used in any string
def test_4(*strings: str):
    st1 = set()
    for strin in strings:
        st1 |= set(strin)
    st = {i for i in string.ascii_lowercase}
    return sorted(st.difference(st1))
