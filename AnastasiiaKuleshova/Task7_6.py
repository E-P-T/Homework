# Task 7.6
# Create console program for proving Goldbach's conjecture. Program accepts number for input and print result.
# For pressing 'q' program succesfully close. Use function from Task 5.5 for validating input, handle all
# exceptions and print user friendly output.
import sys


class Math_Utils:

    @staticmethod
    def is_prime(num: int):
        i = 2
        while i < num:
            if num % i == 0:
                return False
            i += 1
        return True


class Goldbach:

    @staticmethod
    def goldbach_resolve(num: int):
        for i in range(2, num):
            if Math_Utils.is_prime(i):
                if Math_Utils.is_prime(num - i):
                    print(num, '=', i, '+', num - i)
                    return i, num - i
        return None


print(Math_Utils.is_prime(-sys.maxsize - 1))
