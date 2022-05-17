import time
from contextlib import contextmanager


def decor(func):
    def wrapper():
        name = "log.txt"
        start_time = time.perf_counter()
        func(name)
        with func(name) as file:
            file.write(f"{round(time.perf_counter() - start_time, 6)} seconds left for execution)")
    return wrapper()

@decor
@contextmanager
def manager(name):
    try:
        f = open(name, mode="w")
        yield f
    except OSError:
        print("Something went wrong")
    finally:
        f.close()



