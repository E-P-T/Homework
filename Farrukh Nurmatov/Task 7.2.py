"""Implement context manager for opening and working with file,
including handling exceptions with @contextmanager decorator."""
from contextlib import contextmanager


@contextmanager
def writing_logs(folder):
    try:
        print("Beginning writing logfile.....")
        file = open(folder + "log.txt", "w")
        yield file
    except OSError as exc:
        print(f"We have an error {exc}")
    finally:
        print("Writing is finished!")
        file.close()


if __name__ == '__main__':
    with writing_logs("folder/") as log_file:
        log_file.write("Log has been written!")
