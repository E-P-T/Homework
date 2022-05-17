
def endless_fibo():
    first = 1
    res = 0
    while True:
        now = res + first
        yield now
        first = res
        res = now




gen = endless_fibo()
# while True:
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
