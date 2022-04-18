"""Create a program that asks the user for a number and then prints out a list of all the
   [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
    Examples:
    Input: 60
    Output: [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]"""


def divisors_lst(num: int):

    """Function takes integer number to input and return list of divisors."""

    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


if __name__ == '__main__':
    number = int(input("Input:"))
    print("Output:", divisors_lst(number), sep=" ")