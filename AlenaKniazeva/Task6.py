"""This program converts a given tuple of positive integers into an integer"""

def number(inp):
    res = 0
    for i in range(len(inp),0,-1):
        res += int(inp[i-1])*10**(len(inp)-i)
    return res

if __name__ == "__main__":
    inp = tuple(input("Enter a tuple: ").strip("()").replace(", ",""))
    print("Common integer is: {}".format(number(inp)))