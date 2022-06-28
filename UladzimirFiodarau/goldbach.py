# Create console program for proving Goldbach's conjecture. Program accepts number for input and print result.
# For pressing 'q' program succesfully close. Use function from Task 5.5 for validating input,
# handle all exceptions and print user friendly output.
# The conjecture states that every even number starting with 4 can be expressed as the sum of two prime numbers.
class CustomException(BaseException):

    def __init__(self, error_message: str = ''):
        self.message = error_message

    def __str__(self):
        return str(self.message)


class TypeException(CustomException):
    pass


class EmptyException(CustomException):
    pass


class ValueException(CustomException):
    pass


def is_even(num: int = None) -> bool:
    if num is None:
        raise EmptyException("Function requires directly one integer argument")
    elif not isinstance(num, int):
        raise TypeException("Wrong argument type, must be an integer")

    return num % 2 == 0


def get_primes(num: int = None) -> list:
    """
    The function takes a positive integer and returns a list of primes in range [2, integer + 1)
    :param num: input integer
    :return: list of corresponding primes
    """
    if num is None:
        raise EmptyException("Function requires directly one integer argument")
    assert isinstance(num, int) and num >= 0, "Wrong argument type, must be a positive integer"
    primes = list(range(2, num + 1))
    for number in primes:
        i = 2
        while number * i <= primes[-1]:
            if number * i in primes:
                primes.remove(number * i)
            i += 1
    return primes


def find_goldbach(num: int = None) -> tuple:
    """
    the function takes an integer and if it is a positive integer greater or equal to 4 then
    returns a tuple that consists of the integer and a list of two prime numbers which sum forms the integer
    :param num: input integer
    :return:
    """
    if is_even(num):
        if num < 4:
            raise ValueException("Input integer doesn't satisfy conjecture assumings")
        else:
            primes = get_primes(num)
            combinations = [[x, num - x] for x in primes if num - x in primes]
            return num, max(combinations, key=lambda x: x[0])
    else:
        raise ValueException("Input integer doesn't satisfy conjecture assumings")


def get_input():
    return input("Input a positive even integer to prove Goldbach's conjecture for it, or 'q' to exit script: ")


def main():
    while True:
        command = get_input()
        if command in ('q', 'Q'):
            print('Thanks for using script and have a good day')
            break
        else:
            try:
                num = int(command)
            except ValueError:
                num = command if command else None

            try:
                print(find_goldbach(num))
            except ValueException as message:
                print(f'Incorrect input: {message}')
            except EmptyException as message:
                print(f'Incorrect input: {message}')
            except TypeException as message:
                print(f'Incorrect input: {message}')
            except Exception as message:
                print(f'Something got wrong: {message}')


if __name__ == '__main__':
    main()
