"""Implement a function `get_digits(int)` which returns a tuple
of a given integer's digits"""

def get_digits(num):
    # tuple is unmutable object. That's why we append a list
    res = []
    for i in num:
        res.append(int(i))
    return tuple(res)

if __name__ == "__main__":
    inp_num = input("Enter a number: ")
    print("Result tuple is: {}".format(get_digits(inp_num)))