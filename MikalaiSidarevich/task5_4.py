# Task 5.4
# Look through file `modules/legb.py`.

# 1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
# 2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
# 2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.

a = "I am global variable!"


def enclosing_funcion():
    """
    Clause # 1
    """
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)

    return inner_function


def enclosing_funcion_global():
    """
    Clause # 2.1
    """
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        print(a)

    return inner_function


def enclosing_funcion_enclosed():
    """
    Clause # 2.2
    """
    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a
        print(a)

    return inner_function


def main():
    """
    Entry point function.
    """
    enclosing_funcion()()
    enclosing_funcion_global()()
    enclosing_funcion_enclosed()()


if __name__ == '__main__':
    main()
