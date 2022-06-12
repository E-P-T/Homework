a = "I am global variable!"


def enclosing_function():
    a = "I am variable from enclosed function!"

    def inner_function():
        # global a # task 2.1
        # solution of the task 2.1: leave only the line "print(a)"
        print(a)

    inner_function() # task 1
