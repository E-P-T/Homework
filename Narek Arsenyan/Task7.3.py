from contextlib import ContextDecorator
import time

class TimeMeasurement(ContextDecorator):
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
        self.startTime = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stopTime = time.perf_counter()
        self.runTime = self.stopTime - self.startTime
        str = '{funcName} function run for {runTime:.3f} seconds'.format(funcName = self.funcName, runTime = self.runTime)
        print(str)
        self.file.write(str)
        self.file.write('\n')
        if self.file:                                               
            self.file.close()
        return True


@TimeMeasurement()
def sampleFunction():
    counter = 0
    for i in range(10000000):
        counter += 1
    return counter

sampleFunction()
