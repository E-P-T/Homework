#! /usr/bin/env python
# TODO: Implement class-based context manager for opening and working with file
# including handling exceptions. Do not use 'with open()'.
#  Pass filename and mode via constructor.


"""
task_1.py: Implemented class-based context manager for opening and working with
file including handling exceptions and some tests statements.
"""


class FileManager:
    """
    FileManager: class-based context manager for opening and working with file
    including handling exceptions and some tests statements.
    """
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        try:
            self.fileobj = open(self.filename, self.mode)
            return self.fileobj
        except FileNotFoundError as not_found_error:
            print(not_found_error)

    def __exit__(self, exception, value, trace):
        if hasattr(self, 'fileobj'):
            self.fileobj.close()


if __name__ == '__main__':
    with FileManager('task_1.py') as fileobj:
        if fileobj:
            source_code = fileobj.read()
            print(source_code)
