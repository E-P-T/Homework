#!/usr/bin/python3
print('Python Practice - Session 2')
print('Task 2.3 Create a program that asks the user for a number and then prints out a list of all the divisors of that number.')

start = True

while start:
    num = input('Type any number to receive all the divisors of that number: ')

    if num.isdecimal():
        num = int(num)
        divisors_of_num = set()

        for i in range(1, num+1):
            if num % i == 0:
                divisors_of_num.add(i)

        print(f'The divisors of {num} are: {set(sorted(divisors_of_num))}')
        start = False
    else:
        print('Please, make sure to type an integer')