"""This program contains a function `split_by_index` which splits
the `s` string by indexes specified in `indexes`"""

def split_by_index(s,index):
    res = []
    start = 0 # point at start of the string element, which should be appended
    # split string by indexes
    for i in range(len(index)):
        res.append(s[start:index[i]])
        start = index[i]
    # append the rest of the string
    if start != len(s): res.append(s[start : len(s)])
    return res

if __name__ == "__main__":
    # read a string
    inp_s = input("Enter a string: ")
    # read indexes until the Enter will be entered
    list_ind = []
    while True:
        s = input("Enter an index: ")
        try:
            ind = int(s)
            # only valid indexes will be appended
            if ind >= len(inp_s):
                continue
            else:
                list_ind.append(ind)
        except:
            break
    print("Splited text is: {}".format(split_by_index(inp_s, list_ind)))