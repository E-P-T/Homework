import itertools
import string

mock = ["hi", "myi", "Darling", "Pythonist"]

def test_1_1(*strings):
    finalSet = set(strings[0])
    for i in strings:
        finalSet = set(i).intersection(finalSet)
    return list(finalSet)

def test_1_2(*strings):
    finalSet = set(strings[0])
    for i in strings:
        finalSet = set(i).union(finalSet)
    return list(finalSet)


def test_1_3(*strings):
    finalSet = set()
    for i in list(itertools.combinations(strings, 2)):
        finalSet = finalSet.union(set(i[0]).intersection(set(i[1])))
    return list(finalSet)


def test_1_4(*strings):
    alphabet = string.ascii_letters
    chars = test_1_2(*strings)
    return list(set(alphabet).difference(set(chars)))


print(test_1_1(*mock))
print(test_1_2(*mock))
print(test_1_3(*mock))
print(test_1_4(*mock))
