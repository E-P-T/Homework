# Task 4.3
# Implement a function which works the same as `str.split` method (without using `str.split` itself, ofcourse).

def split_string(string: str, separator: str = ' \n\t') -> list[str]:
    """
    The function takes a string as an argument and a string as a separator, then splits the string into a list of
    substrings that were using given separator as a delimiter. The default separator is any whitespace.
    :param string: string taken
    :param separator: string that is used as a separator for input string
    :return: a list of substrings of input string
    :raises AssertionError if input is not string type
    """

    assert isinstance(string, str) and isinstance(separator, str), 'Incorrect input. both arguments must be strings'
    result = [] if string else ['']
    if separator != ' \n\t':
        while string:
            if separator not in string:
                result.append(string)
                return result
            i = string.find(separator)
            result.append(string[:i])
            string = string[i + len(separator):]
        return result
    else:
        result = []
        tmp = ''
        for symbol in string:
            if symbol not in separator:
                tmp += symbol
            elif tmp:
                result.append(tmp)
                tmp = ''
        if tmp:
            result.append(tmp)
        return result

# s = ""
# print(split_string(s))
# print(s.split())

# s = ""
# print(split_string(s, 'v'))
# print(s.split('v'))

# s = 'bramvbramvzumvclackvfoov vvvbar'
# print(split_string(s, 'v'))
# print(s.split('v'))

# s = 'bramvbramvzumvclabkvfoovbvvvbar'
# print(split_string(s, 'b'))
# print(s.split('b'))

# s = 'bramvbramvzumvclabkvfoovbvvvbar'
# print(split_string(s))
# print(s.split())

# s = 'bramvbramvzumvclabkvfoovbvvvbar'
# print(split_string(s, 'i'))
# print(s.split('i'))

# s = 'bam bibom bim    bibim \t bam'
# print(split_string(s))
# print(s.split())

# s = 'bam bibom bim    bibim \t bam'
# print(split_string(s))
# print(s.split())
