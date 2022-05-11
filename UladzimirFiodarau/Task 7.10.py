# ### Task 7.10
# Implement a generator which will generate odd numbers endlessly.
def endless_generator():
    """
    a generator which generates odd numbers endlessly
    """
    value = 1
    while True:
        yield value
        value += 2


if __name__ == '__main__':
    gen = endless_generator()
    while True:
        print(next(gen), end=' ')
# >>> 1 3 5 7 ... 128736187263 128736187265 ...
