a = "I am global variable!"


def enclosing_function():
    a = "I am variable from enclosed function!"

    def inner_function():      
        #a = "I am local variable!"
        #nonlocal a
        print(a)
    return inner_function
