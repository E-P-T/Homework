from curses.ascii import isalpha
import string


def get_letters(*args: str) -> list[set]:
    chars = []

    for arg in args:
        arg_letters = set()
        arg_letters_itr = filter(lambda x: isalpha(x), arg)

        for letter in arg_letters_itr:
            arg_letters.add(letter.lower())
        chars.append(arg_letters)

    return chars

def test_1_1(*args: str) -> set:
    alphabet = { c for c in string.ascii_lowercase}
    chars = get_letters(*args)

    res = alphabet
    for el in chars:
        res = res & el

    return res

def test_1_2(*args: str) -> set:
    chars = get_letters(*args)

    res = set()
    for el in chars:
        res = res | el
    
    return res

def test_1_3(*args: str) -> set:
    chars = get_letters(*args)

    occurences = {}

    for el in chars:
        for chr in el:
            if chr not in occurences:
                occurences[chr] = 1
            else:
                occurences[chr] += 1

    res = {chr for chr, num in filter(lambda tup: tup[1] > 1, occurences.items())}
    return res

def test_1_4(*args: str) -> set:
    alphabet = { c for c in string.ascii_lowercase}
    persistent = test_1_2(*args)

    return alphabet - persistent

    

test_strings = ["hello", "world", "python", ]
print(test_1_1(*test_strings))
print(test_1_2(*test_strings))
print(test_1_3(*test_strings))

valid = {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
outcome = test_1_4(*test_strings)
print(outcome)
print(outcome == valid)

test_1_1()
