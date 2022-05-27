def endless_fib_generator():
    previous = 0
    current = 1
    while True:
        yield current
        current, previous = current + previous, current

if __name__ == "__main__":
    g = endless_fib_generator()
    for n in g:
        print(n)