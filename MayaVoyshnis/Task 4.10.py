def generate_squares(number):
    return {x: x ** 2 for x in range(1, number + 1)}


if __name__ == '__main__':
    print(generate_squares(5))
