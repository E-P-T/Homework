# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
import string


def string_char_intersection(*args):
    ''' characters that appear in all strings '''
    return set(args[0]).intersection(*args[1:])
    output = set()

    for char in args[0]:
        in_all = True
        for string in args[1:]:
            if char not in string:
                in_all = False
                break

        if in_all:
            output.add(char)

    return output


def string_char_union(*args):
    ''' characters that appear in at least one string '''
    return set(args[0]).union(*args[1:])


def string_char_appear_in_two_strings(*args):
    ''' characters that appear at least in two strings '''
    global string

    output = set()

    for char in string.ascii_lowercase:
        counter = 0
        for string_param in args:
            if char in string_param:
                counter += 1

            if counter > 1:
                break

        if counter > 1:
            output.add(char)

    return output


def string_char_not_used(*args):
    ''' characters of alphabet, that were not used in any string '''
    global string

    output = set()

    for char in string.ascii_lowercase:
        used = False
        for string_param in args:
            if char in string_param:
                used = True
                break

        if not used:
            output.add(char)

    return output


if __name__ == '__main__':
    test_strings = ["hello", "world", "python", ]

    print(string_char_intersection(*test_strings))
    print(string_char_union(*test_strings))
    print(string_char_appear_in_two_strings(*test_strings))
    print(string_char_not_used(*test_strings))
