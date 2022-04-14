### Task 2.3
### Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
### Examples:
### Input: 60
### Output: [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]

def calculate_divisors():
    """
    The function asks user to input an integer and returns an ordered from lower to higher list of its divisors.
    If the input is not an integer, the function raises an exception.
    :param n: taken positive integer
    :return: ordered list of divisors of processed integer
    """
    n = input('Введите целое положительное число\n')
    try:
        number = int(n)
        if number < 0:
            raise TypeError('Неверный ввод, необходимо ввести целое положительное число')
        result = []
        for i in range(1, number // 2 + 1):
            if number % i == 0:
                result.append(i)
        result.append(number)
        return result
    except:
        return 'Неверный ввод, необходимо ввести целое положительное число'

print(calculate_divisors())