# Task 7.3
# Implement decorator with context manager support for writing
# execution time to log-file. See contextlib module.

import time
from AnastasiiaKuleshova.Task2 import open_file


def execution_time_log(func):
    def current_milli_time():
        return round(time.time() * 1000)

    def execution_time(*args, **kwargs):
        start = current_milli_time()
        func(*args, *kwargs)
        end = current_milli_time()
        result_time = end - start
        with open_file(".\\data\\timelog_file.txt", 'a') as file:
            file.write(f"{func.__name__} execution time is {result_time}\n")

    return execution_time


@execution_time_log
def calculate_square(x):
    time.sleep(x / 1000)
    return x * x * x


calculate_square(5)
