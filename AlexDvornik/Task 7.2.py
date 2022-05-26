"""
Task 7.2
Implement context manager for opening and working with file,
including handling exceptions with @contextmanager decorator.
"""
from contextlib import contextmanager


@contextmanager
def file_handler(file_path, mode):
    try:
        file = open(file_path, mode=mode)
        yield file
    except FileNotFoundError as error:
        print("An exception occurred: ", error)
    except AttributeError as error_:
        print("An exception occurred: ", error_)
    else:
        file.close()


names = [
    "Richard",
    "Bighead",
    "Gilfoyle",
    "Dinesh"
]
with file_handler('data/data.txt', "a") as inf:
    for name in names:
        inf.writelines(f"{name}" + '\n')



