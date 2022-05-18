"""
Create console program for proving Goldbach's conjecture.
Program accepts number for input and print result.
For pressing 'q' program succesfully close.
Use function from Task 5.5 for validating input, handle all exceptions
and print user friendly output.
"""

from Task7_5 import if_even
from sympy import isprime

def conjecture (num):
    if num != 'q':
        try:
             inum = int(num)
        except ValueError:
            print("It's not a number!")
        else:
            if if_even(inum) == True:
                a = []
                for i in range(1,inum):
                    if isprime(i) == True and isprime(inum-i) == True:
                        a.append(i)
                        a.append(inum-i)
                        return a

if __name__ == "__main__":
    num = None
    while num != 'q':
        num = input("Enter an integer number or 'q' for exit: ")
        result = conjecture(num)
        print ("Components of Goldbach's conjecture: {}".format(result))