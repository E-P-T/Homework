# Task 2.3
# Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
# Examples:
# ```
# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
# ```

while True:
    try:
        number = int(input("Enter a number: "))
        if number < 1:
            raise ValueError
        break
    except:
        print("Invalid number, try again")

# All numbers are divisible by 1
divisors = [1]

for i in range(2, number // 2 + 1):
    if number % i == 0:
        divisors.append(i)

# All numbers are divisible by themselves
divisors.append(number)

print(divisors)
