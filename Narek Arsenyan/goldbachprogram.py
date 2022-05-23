class MyException(Exception):
    def __init__(self, msg = ''):
        self.msg = msg

    def __str__(self):
        return self.msg


class BoolException(MyException):
    pass


class StringException(MyException):
    pass


class TypeException(MyException):
    pass


class EmptyException(MyException):
    pass


def isEven(num = None):
    if num is None:
        raise EmptyException('One argument required')
    elif isinstance(num, str):
        raise StringException('Got string argument. Argument must be integer')
    elif isinstance(num, bool):
        raise BoolException('Got boolean argument. Argument must be integer')
    elif not isinstance(num, int):
        raise TypeException('Unsupported argument type. Argument must be integer')

    return num % 2 == 0


def isPrime(num = None):
    if num == None:
        raise EmptyException('One argument required')
    if not isinstance(num, int):
        raise TypeException('Unsupported argument type. Argument must be integer')
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def primesList(end = None):
    if end == None:
        raise EmptyException('One argument required')
    if not isinstance(end, int):
        raise TypeException('Unsupported argument type. Argument must be integer')

    primeValues = []
    for i in range(2, end + 1):
        if isPrime(i):
            primeValues.append(i)
    return primeValues


def goldbach(num):
    if num == None:
        raise EmptyException('One argument required')
    if not isinstance(num, int):
        raise TypeException('Unsupported argument type. Argument must be integer')

    if num > 2 and isEven(num):
        primes = primesList(num)
        gValue = [num]
        for i in primes:
            if isPrime(num - i):
                gValue.append([i, num - i])
                return gValue
    else:
        raise MyException('Argument is not supported. Please read homework')


def userInput():
    return input('Find goldbach representation of number by entering number. Press "q" to quit:\n')


def consoleProgram():
    while True:
        inputValue = userInput()
        if inputValue == 'q':
            print('You quitted program. Bye-bye')
            return
        else:
            try:
                number = int(inputValue)
            except:
                number = inputValue

            try:
                print(goldbach(number))
            except MyException as msg:
                print('Error: {msg}'.format(msg = msg))
            except Exception:
                print('Something went wrong')
