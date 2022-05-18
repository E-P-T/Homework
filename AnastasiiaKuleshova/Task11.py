# Task 7.11
# Implement a generator which will geterate Fibonacci numbers endlessly. Example:
#
# gen = endless_fib_generator()
# while True:
#     print(next(gen))
# >>> 1 1 2 3 5 8 13 ...
import time


def fibonacci_endless():
    f0 = 0
    f1 = 1
    # result = 0
    while True:
        result = f1 + f0
        yield result
        f0 = f1
        f1 = result


gen = fibonacci_endless()
while True:
    print(next(gen), ' ')
    time.sleep(1)
