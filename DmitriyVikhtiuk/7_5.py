class CustomClass(BaseException):
    pass


def foo(number):
        if number % 2 == 0:
            print("even")
        else:
            print("not even")

try:
    foo("str")
except TypeError as er:
    raise er from CustomClass("invalid type!")
try:
    fo(4)
except NameError as er:
    raise er from CustomClass("Invalid name!")
try:
    foo.a
except AttributeError as er:
    raise er from CustomClass("Functions can not have attributes")






