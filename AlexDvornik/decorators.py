from time import perf_counter


def time_logger(path_to_logfile, name):
    def log(func):
        def wrapped(*args, **kwargs):
            start_time = perf_counter()
            func(*args, **kwargs)
            end_time = perf_counter() - start_time
            with open(path_to_logfile, 'a') as f:
                f.write(f"{name}: {str(round(end_time, 2))}" + '\n')
        return wrapped
    return log
