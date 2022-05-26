"""
Task 7.11
Implement a generator which will generate Fibonacci numbers
"""
from time import sleep


def endless_fib_generator():
    fib1 = fib2 = 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


gen = endless_fib_generator()
while True:
    print(next(gen), end=' ')
    sleep(1)
