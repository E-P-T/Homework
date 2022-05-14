def split(my_string, char_del):
    word = ''
    res = []
    for char in my_string:
        if char != char_del:
            word += char
        elif char == char_del:
            res.append(word)
            word = ''
    res.append(word)
    return res


if __name__ == '__main__':
    print(split(input('Input your string: '), input('Input your char: ')))
