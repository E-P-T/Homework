import re


def string_to_list(string, separator=' ', maxsplit=-1):
    output = []
    # Python > 3.9
    #string = string.removesuffix(separator).removeprefix(separator)

    # Python < 3.8
    string = string[len(separator):] if string.startswith(
        separator) else string
    string = string[:-len(separator)] if string.endswith(separator) else string

    separator_pos = [i for i in range(len(string))
                     if string.startswith(separator, i)]

    print(separator_pos)

    # combine list from substrings
    i = 0
    while i <= len(separator_pos):
        if maxsplit != -1 and i == maxsplit:
            break

        if i == 0:
            output.append(string[:separator_pos[i]])
        elif i == len(separator_pos):
            output.append(string[separator_pos[i-1]+len(separator):])
        else:
            output.append(string[separator_pos[i-1] +
                          len(separator):separator_pos[i]])
        i += 1

    return output


print(string_to_list(' string to be to splitted ', ' ', maxsplit=-1))
