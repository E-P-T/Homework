"""This program contains a function that takes a number as
an argument and returns a dictionary, where the key is a number
and the value is the square of that number"""

def generate_squares(num):
    return {i:i**2 for i in range(num+1)}

if __name__ == "__main__":
    num = int(input("Enter an integer number: "))
    print("Result dictionary: {}".format(generate_squares(num)))