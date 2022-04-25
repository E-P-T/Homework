"""This program contains a function `foo(List[int]) -> List[int]` which, given a list of
integers, return a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array except the one at `i`"""

from math import prod

def foo(*inp_list):
    return [prod(inp_list[:i]+inp_list[i+1:]) for i in range(len(inp_list))]

if __name__ == "__main__":
    inp_list = []
    while True:
        try:
            s = int(input("Enter an integer element: "))
            inp_list.append(s)
        except:
            break
    print("Result list: {}".format(foo(*inp_list)))
