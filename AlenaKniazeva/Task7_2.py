"""
Implement context manager for opening and working with file, including handling
exceptions with @contextmanager decorator.
"""

from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    except BaseException as err:
        # context manager prints the error, if it occures
        print(f'Error: {err}')
        f.close()

def main():
    with open_file("test.txt", 'w') as f:
        f.write("My")
    with open_file('demo.txt', 'w') as f:
        f.undefined_function()

if __name__ == '__main__':
    main()