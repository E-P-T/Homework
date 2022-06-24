import re


def inverter(text):
    result = ''
    for c in text:
        if c == '\'':
            c = '\"'
        elif c == '\"':
            c = '\''
        result += c

    return result


inputstr = input()
print(inverter(inputstr))