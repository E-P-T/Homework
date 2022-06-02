# Task 7.6
# Create console program for proving Goldbach's conjecture.
# Program accepts number for input and print result.
# For pressing 'q' program succesfully close.
# Use function from Task 5.5 for validating input, handle all exceptions and print user friendly output.

class CustomBaseExeption(BaseException):
    pass


class FloatException(CustomBaseExeption):
    pass


class StringException(CustomBaseExeption):
    pass


class ListException(CustomBaseExeption):
    pass


class EvenError(Exception):
    pass


def is_even(n):
    """
    Check if `n` is even number.
    Raises FloatException, StringException, ListException, Exception if `n` has invalid type.
    """
    if isinstance(n, int):
        return n % 2 == 0
    elif isinstance(n, float):
        raise FloatException(f"'{n}' is a float, it should be an integer'")
    elif isinstance(n, str):
        raise StringException(f"'{n}' is a string, it should be an integer'")
    elif isinstance(n, list):
        raise ListException(f"'{n}' is a list, it should be an integer'")
    else:
        raise Exception("Input value should be an integer")


def is_prime(n):
    """
    Check if `n` is prime number.
    """
    isprime = True
    if n < 2:
        isprime = False
    elif n in [2, 3]:
        isprime = True
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                isprime = False
                break
    return isprime


def goldbach(n):
    """
    Check Goldbach's conjecture for `n` even number.
    Return a list of 2 prime numbers that compose `n`.
    """
    if not is_even(n):
        raise EvenError("number should be even")
    if n < 4:
        raise ValueError("number should be >= 4")

    result = [None, None]
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            result = [i, n - i]
            break
    return result


def main():
    """
    Entry point function.
    """
    while True:
        n = input("Enter a number ('q' for exit): ").lower()
        if n == 'q':
            break
        try:
            n = int(n)
            gb = goldbach(n)
        except (ValueError, EvenError, CustomBaseExeption) as e:
            print(f"Error: {e}")
        else:
            print(f"Goldbach's conjecture: {n} = {gb[0]} + {gb[1]}")


if __name__ == '__main__':
    main()
