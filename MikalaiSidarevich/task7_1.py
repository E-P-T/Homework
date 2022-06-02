# Task 7.1
# Implement class-based context manager for opening and working with file, including handling exceptions.
# Do not use 'with open()'. Pass filename and mode via constructor.

class CustomFileMgr:
    """Class-based context manager for opening and working with file."""

    def __init__(self, fname, mode='r'):
        """
        Initialize context manager with file name `fname` and file mode `mode`.
        """
        self.fname = fname
        self.mode = mode

    def __enter__(self):
        self.file = open(self.fname, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"{exc_type.__name__}: {exc_value}")
        self.file.close()
        # Suppress an exception
        return True


def create_file(fname="test.txt"):
    """Create dummy test file."""
    with CustomFileMgr(fname, 'w') as mgr:
        mgr.writelines(["Hello\n", "world\n"])


def main():
    """
    Entry point function.
    """
    create_file()
    fname = "test.txt"
    try:
        with CustomFileMgr(fname, 'r+') as mgr:
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
