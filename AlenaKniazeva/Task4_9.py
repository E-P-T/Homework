"""This program contains a bunch of functions which receive a changeable
number of strings and return next parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
4) characters of alphabet, that were not used in any string"""

import string

def test_1_1(*strings):
    set_str = [set(s) for s in strings]
    res = []
    for s in string.ascii_lowercase:
        flag = True
        for str_el in set_str:
            if s not in str_el:
                flag = False
                break
        if flag ==True: res.append(s)
    return res

def test_1_2(*strings):
    set_str = [set(s) for s in strings]
    res = []
    for s in string.ascii_lowercase:
        flag = False
        for str_el in set_str:
            if s in str_el:
                flag = True
                break
        if flag ==True: res.append(s)
    return res 

def test_1_3(*strings):
    set_str = [set(s) for s in strings]
    res = []
    for s in string.ascii_lowercase:
        flag = False
        count = 0
        for str_el in set_str:
            if s in str_el:
                flag = True
                count += 1
            if count >=2: break
        if (flag == True) & (count >= 2): res.append(s)
    return res 

def test_1_4(*strings):
    set_str = [set(s) for s in strings]
    res = []
    for s in string.ascii_lowercase:
        flag = True
        for str_el in set_str:
            if s in str_el:
                flag = False
                break
        if flag ==True: res.append(s)
    return res

if __name__ == "__main__":
    strings = []
    s = True
    while s:
        s = input("Enter a string: ")
        if s:
            strings.append(s)
    print("Characters that appear in all strings: {}".format(test_1_1(*strings)))
    print("Characters that appear in at least one string: {}".format(test_1_2(*strings)))
    print("Characters that appear at least in two strings: {}".format(test_1_3(*strings)))
    print("Characters of alphabet, that were not used in any string: {}".format(test_1_4(*strings)))