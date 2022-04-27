
def replace_quotes(string):
    output = ''
    for char in string:
        if char == '"':
            output += '\''
        elif char == '\'':
            output += '"'
        else:
            output += char

    return output


print(replace_quotes('"Hello" \' there'))
