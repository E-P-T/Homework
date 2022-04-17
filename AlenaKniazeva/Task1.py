"""This program calculates the length of a string
without using the `len` function"""

def length(s):
    count = sum(1 for i in s)
    return count

if __name__ == '__main__':
    input_string = input("Enter the string: ")
    print(f"The length of the string is {length(input_string)} symbols.")