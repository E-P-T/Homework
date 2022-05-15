def get_digits(num: int) -> tuple:
    """ Function to split all the digits of a given `num` and return them as a tuple of integers.
    """
    str_num = str(num)
    digits = list()

    for digit in str_num:
        digits.append(int(digit))
    
    return tuple(digits)


if __name__ == "__main__":
    d = 87178291199
    print(get_digits(d))