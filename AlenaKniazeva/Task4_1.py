"""This program contains a function which receives a string and replaces
all `"` symbols with `'` and vise versa"""

def replacement(s):
    dict = { '"':"'", "'":'"' }  # dictionary with replacements
    new_s = []   # list for symbols of a new string
    for let in s:
        new_s.append(dict.get(let, let)) # append list with updated symbols
    return ''.join(new_s)

if __name__ == "__main__":
    inp_s = input("Enter the string: ")
    out_s = replacement(inp_s)
    print("Output string: {}".format(out_s))