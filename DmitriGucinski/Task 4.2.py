def isPolindrome(string):
    return string[::-1] == string


def isPolindrome1(string):

    reverse_string = ''
    i = 1
    while i <= len(string):
        reverse_string += string[-i]
        i = i + 1

    if reverse_string == string:
        return True

    return False


print(isPolindrome1('racecar'))
