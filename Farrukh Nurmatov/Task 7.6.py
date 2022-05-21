"""Create console program for proving Goldbach's conjecture.
Program accepts number for input and print result. For pressing 'q' program succesfully close.
Use function from Task 7.5 for validating input, handle all exceptions and print user friendly output."""
from Task_7_5 import *


def goldbach(num):
    x, y = 0, 0
    result = 0
    if num % 2 == 0:
        prime = [x for x in range(3, num) if all(x % y != 0 for y in range(2, x))]
        while result != num:
            for i in range(len(prime)):
                if result == num:
                    break
                x = prime[i]
                for j in range(len(prime)):
                    y = prime[j]
                    result = x + y
                    if result == num:
                        break
    return x, y


if __name__ == '__main__':
    while True:
        number = input("Enter any even number:")
        if number == "q":
            break
        else:
            if even_checker(number):
                number = int(number)
                num1, num2 = goldbach(number)
                print(f"Your number is a sum of {num1} and {num2}")
            else:
                print("You should enter even number!")



