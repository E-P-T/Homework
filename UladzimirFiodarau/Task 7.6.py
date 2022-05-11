# Task 7.6
# Create console program for proving Goldbach's conjecture. Program accepts number for input and print result.
# For pressing 'q' program succesfully close. Use function from Task 5.5 for validating input,
# handle all exceptions and print user friendly output.
# The conjecture states that every even number starting with 4 can be expressed as the sum of two prime numbers.
class CustomException(BaseException):

    def __init__(self, error_message=''):
        self.message = error_message

    def __str__(self):
        return self.message


class TypeException(CustomException):
    pass


class EmptyException(CustomException):
    pass


class ValueException(CustomException):
    pass


class StringException(CustomException):
    pass


def is_even(num: int = None) -> bool:
    if num is None:
        raise EmptyException("Function requires directly one integer argument")
    elif isinstance(num, str):
        raise StringException("Got a string as argument, argument must be an integer")
    elif isinstance(num, bool):
        raise BoolException("Got a Boolean as argument, argument must be an integer")
    elif not isinstance(num, int):
        raise TypeException("Wrong argument type, must be an integer")

    return num % 2 == 0

def get_primes(num: int) -> list:
    """
    The function takes an integer and returns a list of primes in range [2, integer + 1)
    :param num: input integer
    :return: list of corresponding primes
    """
    primes = list(range(2, num + 1))
    for number in primes:
        i = 2
        while number * i <= primes[-1]:
            if number * i in primes:
                primes.remove(number * i)
            i += 1
    return primes

def find_goldbach(num: int) -> tuple:
    """
    the function takes an integer and returns
    :param num:
    :return:
    """
    if is_even(num):
        if num < 4:
            raise ValueException("Input integer doesn't satisfy conjecture assumings")
        elif num == 4:
            return 4, [2, 2]
        elif num == 6:
            return 6, [3, 3]
        else:
            primes = get_primes(num)
            combinations = [[x, num - x] for x in primes if num - x in primes]
            return num, max(combinations, key=lambda x: x[0])
    else:
        raise ValueException("Input integer doesn't satisfy conjecture assumings")

def main():
    command = input("Input a positive even integer, or 'q' to exit script: ")
    if command in ('q', 'Q'):
        print('Thanks for using script and have a good day')
    else:
        try:
            num = int(command)
        except:
            num = command

        try:
            print(find_goldbach(num))
        except ValueException as message:
            print(f'Incorrect input: {message}')
        except EmptyException as message:
            print(f'Error ocured during function runtime: {message}')
        except StringException as message:
            print(f'Error ocured during function runtime: {message}')
        except TypeException as message:
            print(f'Error ocured during function runtime: {message}')

        except Exception:
            print('Something got wrong')
        finally:
            main()



if __name__ == '__main__':
    main()