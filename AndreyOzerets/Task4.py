# Task 5.4

a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)

        # Task 2.1
        print(globals()['a'])

    return inner_function


if __name__ == '__main__':
    enclosing_funcion()()
