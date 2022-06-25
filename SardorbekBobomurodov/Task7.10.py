import time


def endless_generator():
    i = 1
    while True:
        yield i
        i += 2


if __name__ == "__main__":
    arr = endless_generator()
    while True:
        print(next(arr))