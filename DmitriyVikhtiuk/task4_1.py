a = "I am global variable!"


def enclosing_funcion(flag=0):
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)


    inner_function()

enclosing_funcion()