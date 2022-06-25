import time


def endless_fib_generator():
    a = 0
    b = 1
    c = a + b

    while True:
        yield c
        temp = a
        a = c
        b = temp
        c = a + b


if __name__ == "__main__":
    arr = endless_fib_generator()
    while True:
        print(next(arr))
        time.sleep(1)
