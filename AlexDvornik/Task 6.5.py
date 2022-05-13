"""
Task 4.6

A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance.
Implement singleton logic inside your custom class using a method to initialize class instance.

Example:
p = Sun.inst()
f = Sun.inst()
 p is f
True
"""


class Sun(object):
    __instance = None

    def __init__(self):
        pass

    @classmethod
    def inst(cls):
        if cls.__instance is None:
            cls.__instance = super(Sun, cls).__new__(cls)
        return cls.__instance


p = Sun.inst()
print(p)
f = Sun.inst()
print(f)
print(f is p)
