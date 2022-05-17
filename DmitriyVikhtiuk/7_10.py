
def endless_generator():
    res = 1
    while True:
        yield res
        res += 2


gen = endless_generator()
while True:
    print(next(gen))
