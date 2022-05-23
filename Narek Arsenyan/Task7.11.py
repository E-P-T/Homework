def endless_fib_generator():
    prevValue = 0
    curValue = 1
    while True:
        curValue += prevValue
        prevValue = curValue - prevValue
        yield prevValue

gen = endless_fib_generator()
for i in range(100):
    print(next(gen), end=' ')
