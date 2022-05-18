"""
Implement function for check that number is even, at least 3.
Throw different exceptions for this errors.
Custom exceptions must be derived from custom base exception(not Base Exception class).
"""

class CustomBaseExept (BaseException):
    def __init__(self):
        self.mes = "Common error occurs"

    def __str__(self):
        return "Error: {}".format(self.mes)

class NotEvenExcept (CustomBaseExept):
    def __init__(self):
        self.mes = "The number is not an even number"

class LessThreeExept (CustomBaseExept):
    def __init__(self):
        self.mes = "The number is less than 3"

class NotNum(CustomBaseExept):
    def __init__(self):
        self.mes = "It's not an integer number"

def if_even (num):
    try:
        if not isinstance(num, int):
            raise NotNum
        elif num<3:
            raise LessThreeExept
        elif num % 2 == 1:
            raise NotEvenExcept
    except NotNum as mes:
        print(mes)
        return False
    except LessThreeExept as mes:
        print(mes)
        return False
    except NotEvenExcept as mes:
        print(mes)
        return False
    else:
        return True


def main():
    number = ["str", 1.25, 1, 5, 8]
    for i in number:
        if if_even(i) == True:
            print("The number is even!")

if __name__ == '__main__':
    main()