# ### Task 7.4
# TODO: Implement decorator for suppressing exceptions. If exception not occur write log to console.

def f(func):
    def silence(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
        else:
            print("There is no exception")

    return silence


@f
def mod(a, b):
    print(a / b)


mod(7, 0)
