import string


def test_1_1(*args):
    list =[]
    first_string = args[0]
    args = args[1:]
    flag = " "
    for char in first_string:
        for i in range(len(args)):
            if char in args[i]:
                flag = char
                continue
            else:
                flag = None
                break
        list.append(flag)
    l = [elem for elem in list if type(elem) == str]
    return(l)


def test_1_2(*args):
    list_of_char = [char for word in args for char in word]
    for c in list_of_char:
        while list_of_char.count(c) != 1:
            list_of_char.pop(list_of_char.index(c))

    return list_of_char


def test_1_3(*args):
    list = []
    while len(args) > 1:
        first_string = args[0]
        args = args[1:]
        flag = " "
        for char in first_string:
            for i in range(len(args)):
                if char in args[i]:
                    flag = char
                    continue
            if flag not in list and flag != " ":
                list.append(flag)
    return list

def test_1_4(*args):
    global char_of_strings
    all_chars = string.ascii_lowercase
    alph_list = [char for char in all_chars]
    for elem in char_of_strings:
        alph_list.pop(alph_list.index(elem))
    return alph_list

inp = input("give me your strings, separated by comma like this: hello, world, python  - ")
test_strings = inp.split(", ")

char_of_strings = test_1_2(*test_strings)
print(test_1_1(*test_strings))
print(test_1_2(*test_strings))
print(test_1_3(*test_strings))
print(test_1_4(*test_strings))