# Task 7.6
# Create console program for proving Goldbach's conjecture. Program accepts number for input and print result.
# For pressing 'q' program succesfully close. Use function from Task 5.5 for validating input, handle all
# exceptions and print user friendly output.
from AnastasiiaKuleshova.Task5 import Task5


def is_prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def goldbach_resolve(num):
    for i in range(2, num):
        if is_prime(i):
            if is_prime(num - i):
                print(num, '=', i, '+', num - i)
                return True
    return False


while True:
    number = input("enter a number or press or press 'q' to quit \n")
    if number == 'q':
        break
    if Task5.is_even(int(number)):
        goldbach_resolve(int(number))
        continue
