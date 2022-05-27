from contextlib import contextmanager
from time import time

@contextmanager
def record_time():
    try:
        start_time = time()
        yield
    except Exception as exc:
        print(exc)
    else:
        file_name = __file__.split("\\")[-1][:-3] + ".log"
        f = open(file_name, "a")

        end_time = time()
        execution_time = end_time - start_time

        f.write(f"{execution_time:.2f}\n")
    finally:
        f.close()


with record_time():
    for i in range(10000):
        i = i / 0
    