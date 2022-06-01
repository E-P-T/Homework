a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"  # 2.1 - global a; 2.2 - nonlocal a
        print(a)

    return inner_function
