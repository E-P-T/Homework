#! /usr/bin/env python
# TODO: Implement context manager for opening and working with file,
# including handling exceptions with @contextmanager decorator.


"""
task_2.py: Implemented context manager for opening and working with file,
including handling exceptions with @contextmanager decorator and some test
statements.
"""


from contextlib import contextmanager


@contextmanager
def file_manager(filename, mode='r'):
    """
    file_manager: context manager for opening and working with file, including
    handling exceptions with @contextmanager decorator and some test statements
    """
    try:
        fileobj = open(filename, mode)
        yield fileobj
        fileobj.close()
    except FileNotFoundError as not_found_error:
        print(not_found_error)
        yield None


if __name__ == '__main__':
    with file_manager('task_2.py') as fileobj:
        if fileobj:
            source_code = fileobj.read()
            print(source_code)
