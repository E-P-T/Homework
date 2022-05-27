from contextlib import contextmanager

@contextmanager
def custom_file_handling(filename, mode = "r"):
    """ Function that implements a basic file operations as a context manager. """
    try:
        f = open(filename, mode)
        yield f
    except Exception as exc:
        print(exc)
    else:
        print("The operation was performed successfully!")
    finally:
        f.close()


with custom_file_handling("task.txt") as f:
    print(f.read())
    
