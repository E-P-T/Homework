# Task 7.4
# Implement decorator for supressing exceptions. If exception not occure write log to console.

def exception_supress(func):
    def inner_exeption_supress(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            pass
            # print(e)
        else:
            print("exception didn't occure")

    return inner_exeption_supress


@exception_supress
def my_func(line):
    print(line + "hello")


my_func(3 + 4)
my_func("hello")
