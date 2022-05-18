"""
Implement a generator which will geterate
[Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) endlessly.
gen = endless_fib_generator()
while True:
    print(next(gen))
>>> 1 1 2 3 5 8 13 ...

"""

def endless_fib_generator():
    prev, num = 0, 1
    yield prev
    yield num
    fib = prev+num
    while True:
        yield fib
        prev, num = num, fib
        fib = prev+num

if __name__ == "__main__":
    gen = endless_fib_generator()
    while True:
        print(next(gen))