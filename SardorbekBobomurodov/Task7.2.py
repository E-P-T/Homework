from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    try:
        f = open(filename, mode)
        yield f
        f.close()
    except FileNotFoundError as error:
        print(error)
        yield None


if __name__ == '__main__':
    with open_file('Task7.1.py', "r") as f:
        if f:
            source_code = f.read()
            print(source_code)
