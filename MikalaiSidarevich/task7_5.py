# Task 7.5
# Implement function for check that number is even, at least 3.
# Throw different exceptions for this errors.
# Custom exceptions must be derived from custom base exception(not Base Exception class).

class CustomBaseExeption(BaseException):
    pass


class FloatException(CustomBaseExeption):
    pass


class StringException(CustomBaseExeption):
    pass


class ListException(CustomBaseExeption):
    pass


def is_even(n: int) -> bool:
    """
    Check if `n` is even number.
    Raises FloatException, StringException, ListException, Exception if `n` has invalid type.
    """
    if isinstance(n, int):
        return n % 2 == 0
    elif isinstance(n, float):
        raise FloatException(f"'{n}' is a float, it should be an integer.")
    elif isinstance(n, str):
        raise StringException(f"'{n}' is a string, it should be an integer.")
    elif isinstance(n, list):
        raise ListException(f"'{n}' is a list, it should be an integer.")
    else:
        raise Exception("input value should be an integer.")


def main():
    """
    Entry point function.
    """
    try:
        print(is_even(2))
    except (FloatException, StringException, ListException, Exception) as e:
        exc_type = type(e).__name__
        print(f"{exc_type}: {e}")
    try:
        print(is_even(2.5))
    except (FloatException, StringException, ListException, Exception) as e:
        exc_type = type(e).__name__
        print(f"{exc_type}: {e}")
    try:
        print(is_even("2"))
    except (FloatException, StringException, ListException, Exception) as e:
        exc_type = type(e).__name__
        print(f"{exc_type}: {e}")
    try:
        print(is_even([2, 2.5]))
    except (FloatException, StringException, ListException, Exception) as e:
        exc_type = type(e).__name__
        print(f"{exc_type}: {e}")
    try:
        print(is_even({2: 2.5}))
    except (FloatException, StringException, ListException, Exception) as e:
        exc_type = type(e).__name__
        print(f"{exc_type}: {e}")


if __name__ == '__main__':
    main()
