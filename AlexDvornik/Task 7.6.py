"""
Task 7.6
Create console program for proving Goldbach's conjecture.
Program accepts number for input and print result.
For pressing 'q' program successfully close.
Use function from Task 5.5 for validating input, handle all exceptions and print user-friendly output.
"""
import time
from exceptions import *


class Goldbach:
    def __init__(self, value: int):
        self._number = self.__value_converter(value)

    @staticmethod
    def _is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def _is_valid(self):
        if self._number <= 2:
            print("[+] Not valid value. Program stopped")
            raise ValueBelowTwo
        elif self._number % 2 != 0:
            print("[+] Not valid value. Program stopped")
            raise NotEvenValue
        return True

    def __value_converter(self, value):
        if isinstance(value, str):
            if value.isdigit():
                print("[+] Converting into int...")
                return int(float(value))
            else:
                print("[+] An error occurred. Program stopped")
                raise WrongTypeOfArgument
        else:
            print("[+] You run the program with wrong type")
            raise WrongTypeOfArgument

    def calc(self):
        if self._is_valid():
            print("[+] Value is valid")
            time.sleep(1)
            for i in range(3, self._number):
                if self._is_prime(i):
                    for j in range(i, self._number):
                        if self._is_prime(j):
                            if self._number == i + j:
                                print((i, j))


def main():
    while True:
        n = input("[+] Enter your number: ")
        if n == 'q':
            print("[+] End program")
            break
        else:
            goldbach = Goldbach(n)
            goldbach.calc()


if __name__ == '__main__':
    print("[+] --- Running the program ---")
    time.sleep(1)
    main()
