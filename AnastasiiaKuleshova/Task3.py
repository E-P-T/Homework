# Implement a function which works the same as str.split method (without using str.split itself, ofcourse).

def like_split(line, separator):
    result_list = []
    bypass = 0
    temp_string = ""
    for i in range(0, len(line)):
        if bypass > 0:
            bypass -= 1
            continue
        if line[i] == separator[0] and len(line) >= i + len(separator):
            if line[i: len(separator) +i] == separator:
                bypass = len(separator)-1
                if len(temp_string) > 0:
                    result_list.append(temp_string)
                    temp_string = ""
        else:
            temp_string += line[i]
    if len(temp_string) > 0:
        result_list.append(temp_string)
    print(result_list)


like_split("abcdef", "de")
