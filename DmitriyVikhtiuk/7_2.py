from contextlib import contextmanager




@contextmanager

def fileman(path):
    try:
        f_obj = open(path, mode="w")
        yield f_obj
    except OSError:
        print("Something went wrong!")
    finally:
        f_obj.close()


with fileman("test.txt") as f:
    f.write("Hello")