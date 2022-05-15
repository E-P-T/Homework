def generate_squares(number: int) -> dict:
    """ Function that takes a `number`, generates a dictionary where keys are the numbers from 1 until `number`,
        and pairs are the squares of keys.
        Returns that dictionary.
    """
    squares = {
        n: n * n
        for n in range(1, number + 1)
    }

    return squares


if __name__ == "__main__":
    number = 0
    print(generate_squares(number))
