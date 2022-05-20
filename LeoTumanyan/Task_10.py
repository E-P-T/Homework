### Task 7.10
# TODO: Implement a generator which will generate odd numbers endlessly.

def endless_generator():
    n = 1
    while True:
        yield n
        n += 2


gen = endless_generator()
while True:
    print(next(gen))
# >>> 1 3 5 7 ... 128736187263 128736187265 ...
