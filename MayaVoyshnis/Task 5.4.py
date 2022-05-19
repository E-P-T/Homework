'''
Task 4.4
Look through file modules/legb.py.

Find a way to call inner_function without moving it from inside of enclosed_function.
2.1) Modify ONE LINE in inner_function to make it print variable 'a' from global scope.

2.2) Modify ONE LINE in inner_function to make it print variable 'a' form enclosing function.
'''


a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        # print(globals()['a'])  #2.1
        #nonlocal a #2.2
        print(a)
    return inner_function



if __name__ == '__main__':
    func=enclosing_funcion()
    func()








