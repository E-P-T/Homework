# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. Examples:

# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}

input_number = int(input("Enter number => "))

output = []
for divisor in range(1, input_number+1):
    if input_number % divisor == 0:
        output.append(divisor)

print('Result {}'.format(output))