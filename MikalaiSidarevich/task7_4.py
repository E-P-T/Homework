# Task 7.4
# Implement decorator for supressing exceptions. If exception not occure write log to console.

def suppress(f):
    """
    Decorator for supressing exceptions.
    """
    def inner(n=0):
        try:
            f(n)
        except Exception as e:
            exc_type = type(e).__name__
            print(f"{exc_type}: {e}")
        else:
            print("There are no errors")
    return inner


@suppress
def proc(n=0):
    """
    Dummy exceptions rising.
    """
    if n == 0:
        raise Exception("common exception occured.")
    elif n == 1:
        raise ValueError("invalid value encountered.")
    elif n == 2:
        raise TypeError("invalid value type.")
    elif n == 3:
        raise StopIteration
    else:
        # No errors
        return 0


def main():
    """
    Entry point function.
    """
    proc()
    proc(1)
    proc(2)
    proc(3)
    proc(4)


if __name__ == '__main__':
    main()
