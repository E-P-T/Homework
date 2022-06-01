# Task 4.10
# Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number.
# ```python
# print(generate_squares(5))
# >>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ```

def generate_squares(number: int) -> dict[int, int]:
    """
    Generate a dictionary of squares of the given number.
    """
    return {i: i**2 for i in range(1, number+1)}


def main():
    """
    Entry point function.
    """
    print(generate_squares(0))
    print(generate_squares(5))


if __name__ == '__main__':
    main()
