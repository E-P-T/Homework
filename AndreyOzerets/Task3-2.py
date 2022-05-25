# Task 2.3-2

from typing import List


def get_number(greeting: str) -> int:
    '''Get number from user.'''
    while True:
        try:
            number = int(input(greeting))
            break
        except ValueError:
            print("You entered not a number!!! Try it again...")
    return number


def get_divisors(number: int) -> List[int]:
    '''Get the divisors of a number.'''
    divisors = [i for i in range(1, number+1) if number % i == 0]
    return divisors
