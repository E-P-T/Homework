def split_by_index(string, indexes):
    output = []
    i = 0
    while i <= len(indexes):
        if i > 0 and indexes[i-1] > len(string):
            i += 1
            continue

        if i == 0:
            output.append(string[:indexes[i]])
        elif i == len(indexes):
            output.append(string[indexes[i-1]:])
        else:
            output.append(string[indexes[i-1]:indexes[i]])
        i += 1

    return output


print(
    split_by_index("pythoniscool,isn'tit?", [42, 6, 8, 12, 13, 18])
)
