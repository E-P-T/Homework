### Task 7.2
# TODO: Implement context manager for opening and working with file, including handling
#  exceptions with @contextmanager decorator.

from contextlib import contextmanager


@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()


try:
    with open_file('test.txt', 'r') as d:
        a = d.read()
except Exception as e:
    print(e)
else:
    print(a)
