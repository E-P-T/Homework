import string


def test_1_1(*args):
    temp_set=set()
    for i in range(len(args)):
        temp_set.update(args[i])
    for i in range(len(args)):
        temp_set.intersection_update(set(args[i]))
    return(temp_set)

def test_1_2(*args):
    temp_set=set()
    for i in range(len(args)):
        temp_set.update(args[i])
    return(temp_set)

def test_1_3(*args):
    temp_list=[]
    set_out=set()
    for i in range(len(args)):
        temp_list.append(set(args[i]))
    for i in range(len(temp_list)-1):
        for j in range(1, len(temp_list)):
            if i != j: set_out.update(temp_list[i].intersection(temp_list[j]))
    return(set_out)

def test_1_4(*args):
    temp_set=set()
    alphabet_set=set(string.ascii_lowercase)
    for i in range(len(args)):
        temp_set.update(args[i])
    alphabet_set.difference_update(temp_set)
    return(alphabet_set)

test_strings = ["hello", "world", "python", ]
print(test_1_1(*test_strings))
print(test_1_2(*test_strings))
print(test_1_3(*test_strings))
print(test_1_4(*test_strings))