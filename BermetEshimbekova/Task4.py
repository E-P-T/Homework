### Task 2.3
# Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
# Examples:
# ```
# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
# ```

number = int(input('Input: '))
if number >= 1:
    divisors = [1,number]
    left = 2
    right = number
    while left < right:
        if number % left == 0:
            right = number//left
            divisors.append(left)
            divisors.append(right)
        left += 1
    divisors = list(set(divisors))
    divisors.sort()
    print(divisors)
else:
    print('Please enter natural number')