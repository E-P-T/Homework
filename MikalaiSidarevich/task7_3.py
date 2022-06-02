# Task 7.3
# Implement decorator with context manager support for writing execution time to log-file. See contextlib module.

from contextlib import ContextDecorator
import time


class track_entry_and_exit(ContextDecorator):
    """Decorator with context manager support for writing execution time to log-file."""

    def __init__(self, name, fname="log.txt", mode='a'):
        """
        Initialize context manager with file name `fname` and file mode `mode`.
        """
        self.name = name
        self.fname = fname
        self.mode = mode

    def time_format(self, t, prec=6):
        """
        Convert time given to human readable format. 
        `t` is time in nanoseconds, `prec` is float precision.
        """
        if t > 1e9:
            return f"{round(t*1e-9, prec)} s"
        elif t > 1e6:
            return f"{round(t*1e-6, prec)} ms"
        elif t > 1e3:
            return f"{round(t*1e-3, prec)} mks"
        else:
            return f"{round(t, prec)} ns"

    def __enter__(self):
        self.file = open(self.fname, self.mode)
        self.time = time.time_ns()

    def __exit__(self, exc_type, exc, exc_tb):
        exec_t = time.time_ns() - self.time
        self.file.write(f"'{self.name}' execution time: {self.time_format(exec_t)}\n")
        self.file.close()


@track_entry_and_exit("Business logic #1")
def proc():
    """Dummy business logic."""
    print("-->Business logic #1")
    for i in range(100_000_000):
        pass


def main():
    """
    Entry point function.
    """
    proc()

    with track_entry_and_exit("Business logic #2"):
        print("-->Business logic #2")
        for i in range(100_000_000):
            pass


if __name__ == '__main__':
    main()
