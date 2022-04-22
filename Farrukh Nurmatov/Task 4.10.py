"""Implement a function that takes a number as an argument and returns a dictionary,
where the key is a number and the value is the square of that number."""


def generate_squares(num: int):
    return {i: i ** 2 for i in range(1, num + 1)}


if __name__ == '__main__':
    print(generate_squares(5))