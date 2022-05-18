"""
Task 7.3
Implement decorator with context manager support for writing execution time to log-file.
See contextlib module.
"""

from decorators import time_logger
from custom_context import File


@time_logger('data/log.txt', "main")
def main():
    with File('data/data.txt', "a") as inf:
        inf.writelines("Hello world" + '\n')


if __name__ == "__main__":
    main()
