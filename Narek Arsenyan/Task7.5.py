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


print(isEven(3))
print(isEven(2))
try:
    print(isEven())
except EmptyException as msg:
    print('Error: {msg}'.format(msg = msg))

try:
    print(isEven('2'))
except StringException as msg:
    print('Error: {msg}'.format(msg = msg))

try:
    print(isEven(True))
except BoolException as msg:
    print('Error: {msg}'.format(msg = msg))

try:
    print(isEven({5}))
except TypeException as msg:
    print('Error: {msg}'.format(msg = msg))
