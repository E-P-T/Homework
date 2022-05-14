"""Look through file `modules/legb.py`.
1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function."""

a = "I am global variable!"


def enclosing_function():

    #a = "I am variable from enclosed function!"   # 2.2 the same as in 2.1, but should find in global scope

    def inner_function():
        #a = "I am local variable!"     # 2.1 just put "#" before "a" variable and inner
                                        # function should find it in enclosing scope
        print(a)

    return inner_function()          # 1 - to call inner function we must return it from enclosing function