# ### Task 7.6
# TODO: Create console program for proving Goldbach's conjecture. Program accepts number for input and print result. ' \
#         'For pressing 'q' program successfully close. Use function from Task 7.5 for validating input, handle all ' \
#         'exceptions and print user friendly output.

from Task_5 import *


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def goldbach_conjecture(num):
    if is_even(num):
        prime_list = [n for n in range(2, num) if is_prime(n)]
        for i in prime_list:
            for j in prime_list:
                if i + j == num:
                    print(f'Your input: {num} = {i} + {j}')
                    return


def main():
    user_inp = input("Enter a even number to prove Goldbach's conjecture or press 'q' to quit: ")
    try:
        command = int(user_inp)
        if isinstance(command, int):
            pass
        else:
            raise WrongType(command)
    except ValueError:
        if user_inp == 'q':
            exit(0)
        else:
            print('Error: wrong input')
    except MyError as e:
        print(e)
    else:
        goldbach_conjecture(command)


if __name__ == '__main__':
    while 42:
        main()
