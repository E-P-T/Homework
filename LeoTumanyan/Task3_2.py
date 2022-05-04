# ### Task 2.3.2
# Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
# Examples:
# ```
# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
# ```
def number_divisors():
    num = int(input("Please enter a number: "))
    divisors = list()
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
    print(divisors)