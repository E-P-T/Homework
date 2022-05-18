# Task 7.2
# Implement context manager for opening and working with file,
# including handling exceptions with @contextmanager decorator.
from contextlib import contextmanager
from typing import ContextManager


@contextmanager
def open_file(file_name, mode):
    file = open(file_name, mode)
    try:
        yield file
    except Exception as e:
        print(e)
        raise e
    finally:
        print('FInally')
        file.close()

