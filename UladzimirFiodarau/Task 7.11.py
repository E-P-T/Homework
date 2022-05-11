# Task 7.11
# Implement a generator which will geterate [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) endlessly.

def endless_fib_generator():
    """
    a generator which generates Fibonacci numbers endlessly
    """
    index = 0
    fb = [1, 1]
    while True:
        if index < len(fb):
            yield fb[index]
        else:
            fb.append(fb[index -1] + fb[index - 2])
            yield fb[index]
        index += 1


if __name__ == '__main__':
    gen = endless_fib_generator()
    for i in range(35):
        print(next(gen), end=' ')
# >>> 1 1 2 3 5 8 13 ...
