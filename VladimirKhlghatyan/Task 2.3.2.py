# Task 2.3.2
# Create a program that asks the user for a number and then prints out a list of all the [divisors]
# (https://en.wikipedia.org/wiki/Divisor) of that number.
# Examples:
# ```
# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
# ```


def divisors(nb):
    divs = list()
    for n in range(1, nb + 1):
        if nb % n == 0:
            divs.append(n)
    print(divs)
