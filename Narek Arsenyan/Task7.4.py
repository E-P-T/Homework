from contextlib import ContextDecorator


class ExcSuppressor(ContextDecorator):
    def __init__(self, funcName = None):
        self.funcName = funcName
        self.file = None

    def __call__(self, function):
        if self.funcName is None:
            self.funcName = function.__name__
        return super().__call__(function)

    def __enter__(self):
        try:
            self.file = open('log.txt', 'a')
        except:
            print('Error: could not open (create) log.txt')
        return self

    def __exit__(self, exc_type = None, exc_val = None, exc_tb = None):
        if exc_type is None:
            str = '{funcName} function didn\'t throw exceptions'.format(funcName = self.funcName)
            self.file.write(str)
            print(str)
        else:
            print('Exception "{exc_val}" was supressed'.format(exc_val = exc_val))
        if self.file:
            self.file.close()
        return True


@ExcSuppressor()
def getValue(index):
    lst = [1,2,3,4,5]
    return lst[index]

getValue(3)
getValue(10)
