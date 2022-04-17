# Task 4.3
# Implement a function which works the same as `str.split` method
# (without using `str.split` itself, of course).


def ft_split(input_string, delimiter):
    spl_list = list()
    start = 0
    end = 0

    for i in range(len(input_string)):
        if input_string[i] != delimiter:
            end += 1
            continue
        if input_string[i - 1] != delimiter:
            spl_list.append(input_string[start:end])
        if input_string[i] == delimiter:
            end += 1
            start = end
    return spl_list
