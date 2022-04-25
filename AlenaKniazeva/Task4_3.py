"""This program contains a function which works the same as `str.split` method"""

def split_f(str, sep):
    res_list = []
    len_sep = len(sep)
    start = 0
    for i in range(len(str)):
     #  print(str[i : i+len_sep])
        if str[i : i+len_sep] == sep:
            res_list.append(str[start : i])
            start = i+len_sep
    if start != len(str): res_list.append(str[start : len(str)])
    return res_list

if __name__ == "__main__":
    inp_str = input("Enter a string: ")
    inp_sep = input("Enter a separator: ")
    print("Separated string is : {}".format(split_f(inp_str, inp_sep)))