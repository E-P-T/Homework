# TODO Create console program for proving Goldbach's conjecture.
#  Program accepts number for input and print result.
#  For pressing 'q' program succesfully close.
#  Use function from Task 5.5 for validating input, handle all exceptions and print user friendly output.

class CustomException(Exception):
    pass


class StringException(CustomException):
    pass


class NotIntegerException(CustomException):
    pass


def is_even(number):
    if isinstance(number, str):
        raise StringException("Number is string!")
    elif not isinstance(number, int):
        raise NotIntegerException("Number is not integer!")
    return number % 2 == 0


def gen_primes(number):
    if isinstance(number, str):
        raise StringException("Number is string!")
    elif not isinstance(number, int):
        raise NotIntegerException("Number is not integer!")
    return [i for i in range(2, 10) if all(i % j for j in range(2, i))]


def goldbach(number):
    if is_even(number) and number >= 4:
        primes = gen_primes(number)
        return [(x, y) for x in primes for y in primes if x + y == number]
    else:
        raise ValueError('Not even number')


def main():
    while (number := input('Input a num: ')) != 'q':
        print(goldbach(int(number)))


if __name__ == "__main__":
    main()
