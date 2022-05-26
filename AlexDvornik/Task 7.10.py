"""
Task 7.10
Implement a generator which will generate odd numbers endlessly
"""
from time import sleep


def endless_generator():
    i = 1
    while True:
        yield i
        i += 2


gen = endless_generator()
while True:
    print(next(gen), end=' ')
    sleep(0.5)
