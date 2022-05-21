"""Implement function for check that number is even, at least 3 throw different exceptions for this errors.
Custom exceptions must be derived from custom base exception(not Base Exception class)."""


class ZeroNumber(Exception):
    pass


class NumNotInteger(Exception):
    pass


class NotNumber(Exception):
    pass


def even_checker(num):
    try:
        if num.isalpha():
            raise NotNumber("This is not number, it is characters!")
    except AttributeError:
        if num == 0:
            raise ZeroNumber("Zero is very even number!")
        else:
            a = int(num)
            b = float(num)
            if a > b or a < b:
                raise NumNotInteger("This is not integer number")
    num = int(num)
    return num % 2 == 0


if __name__ == '__main__':
    print(even_checker("4"))
