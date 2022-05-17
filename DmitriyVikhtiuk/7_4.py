def supp_excs(func):
    def wrapper():
        try:
            func()
        except BaseException as err:
            print(f"Exception suppresed: {err} in function '{func.__name__}'")
    return wrapper()

@supp_excs
def foo():
    return 1/0

@supp_excs
def foo_1():
    with open("file.txt", mode="r"):
        pass


