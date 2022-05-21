"""Implement decorator for supressing exceptions. If exception not occure write log to console."""
from contextlib import contextmanager


@contextmanager
def error_handler():
    try:
        print("Starting program execution!")
        yield
    except Exception as exc:
        print(f"Exception found: {exc}")
    else:
        print("No errors found!")
    finally:
        print("Program execution completed!")


if __name__ == '__main__':
    with error_handler() as handler:
        print(10 / 6)
