#! /usr/bin/env python
# TODO: Implement a function that takes a number as an argument
# and returns a dictionary, where the key is a number and the value
# is the square of that number.
# >>> python
# print(generate_squares(5))
# >>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


"""
task_10.py: implemented 3 functions which take number and return dictionary
where key is number and value is square of a number. It also contains speed
tests for these function to measure performance of different approaches.
"""


import timeit
from numpy import average as avg


def generate_squares(number):
    """
    generate_squares: this is the first function of 3 fucntions which returns
    dictionary number: square_of_a_number. It's built with dictionary
    comprehension and operation *.
    """
    return {n: n * n for n in range(1,  abs(number) + 1)}


def generate_squares2(number):
    """
    generate_squares2: this is the second function of 3 fucntions which returns
    dictionary number: square_of_a_number. It's built with loop for and
    operation *.
    """
    result = {}

    for n in range(1, abs(number) + 1):
        result[n] = n * n

    return result


def generate_squares3(number):
    """
    generate_squares3: this is the third function of 3 fucntions which returns
    dictionary number: square_of_a_number. It's built with constructor of class
    dict and built-in function zip and generator expression.
    """
    return dict(
        zip(range(1, abs(number) + 1), (n * n for n in range(1, abs(number) + 1)))
    )


if __name__ == '__main__':
    print(generate_squares(5))  # Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    print(generate_squares2(5))  # Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    print(generate_squares3(5))  # Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    result = timeit.repeat(
        stmt="generate_squares(5)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0005190148001929628

    result = timeit.repeat(
        stmt="generate_squares2(5)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.00046884640032658355

    result = timeit.repeat(
        stmt="generate_squares3(5)",
        number=1000,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.0012430974000380956

    # As we can see function with dict comprehension has the same performing
    # time as function with loop. But the first function more readable than
    # the second. As to the third function it's obviously slower than others.
