"""Implement a generator which will generate odd numbers endlessly."""
from time import sleep


def endless_generator():
    res = 1
    while True:
        yield res
        sleep(3)
        res += 2


if __name__ == '__main__':
    gen = endless_generator()
    while True:
        print(next(gen))
