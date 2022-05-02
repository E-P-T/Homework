# Task 4.6
# A singleton is a class that allows only a single instance of itself to be created and gives access to that created
# instance. Implement singleton logic inside your custom class using a method to initialize class instance.

class Singleton:
    """
    Implements a Singleton class decorator, that raises TypeError when using __call__
    To initialize instance, user needs to use the `inst` method.
    """

    def __init__(self, func):
        self._func = func

    def inst(self):
        """
        On first call, method creates an instance of decorated class and calls its `__init__` method.
        On future calls, the first created instance is returned.
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._func()
            return self._instance

    def __call__(self):
        raise TypeError('Singleton must be created through "instance" method')

@Singleton
class Sun:
    def __init__(self):
        pass


@Singleton
class Moon:
    def __init__(self):
        pass

# p = Sun.inst()
# f = Sun.inst()
# print(type(f))
# # <class '__main__.Sun'>
# print(p is f)
# # True
#
# x = Moon.inst()
# y = Moon.inst()
# print(type(x))
# # <class '__main__.Moon'>
# print(x is y)
# # True
# print(f is y)
# # False
# print(p is f)
# # True
