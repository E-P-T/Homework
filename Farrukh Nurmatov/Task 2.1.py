"""Write a Python program to calculate the length of a string without using the `len` function."""


def my_count(countable_str: str):

    """Function takes string and counts characters, moving through the string in 'for' loop and increasing counter."""

    c = 0
    for char in countable_str:
        c += 1
    return c

if __name__ == '__main__':
    input_string = input("Input:")
    print(f"Output: {my_count(input_string)}")
