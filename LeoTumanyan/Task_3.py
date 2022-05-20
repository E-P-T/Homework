### Task 7.3
# TODO: Implement decorator with context manager support for writing execution time to log-file. See contextlib module.
from contextlib import contextmanager
from time import time, sleep


@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()


@contextmanager
def runtime(description):
    start_time = time()
    try:
        yield
    finally:
        end_time = time()
        run_time = end_time - start_time
        log = open('task3.log', 'a')
        log.write(f"{description} took {run_time} seconds to run.\n")


@runtime("Multiply")
def multiply(a, b):
    sleep(2)
    print(a * b)


multiply(99599, 4956)
