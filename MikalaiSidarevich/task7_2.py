# Task 7.2
# Implement context manager for opening and working with file, including handling exceptions with @contextmanager decorator.

from contextlib import contextmanager


@contextmanager
def custom_mgr(fname, mode='r'):
    """
    Generator context manager.
    Initialize file name with `fname` and file mode with `mode`.
    """
    file = open(fname, mode)
    try:
        yield file
    except Exception as e:
        exc_type = type(e).__name__
        print(f"{exc_type}: {e}")
    file.close()


def create_file(fname="test.txt"):
    """Create dummy test file."""
    with custom_mgr(fname, 'w') as mgr:
        mgr.writelines(["Hello\n", "world\n"])


def main():
    """
    Entry point function.
    """
    create_file()
    fname = "test.txt"
    try:
        with custom_mgr(fname, 'r+') as mgr:
            # Reading
            for line in mgr:
                print(line, end='')

            # Writing
            mgr.write("!\n")
            mgr.seek(0)

            # Trying to get an error
            for line in mgr:
                print(int(line), end='')

    except FileNotFoundError as e:
        exc_type = type(e).__name__
        print(f"{exc_type}: {e}")


if __name__ == '__main__':
    main()
