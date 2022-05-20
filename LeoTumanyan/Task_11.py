# ## Task 7.11 TODO:Implement a generator which will generate [Fibonacci numbers]
#  (https://en.wikipedia.org/wiki/Fibonacci_number) endlessly.


def endless_fib_generator():
    i, j, ret = 0, 1, 1
    while True:
        yield ret
        ret = j + i
        i = j
        j = ret


gen = endless_fib_generator()
while True:
    print(next(gen))
# >>> 1 1 2 3 5 8 13 ...
