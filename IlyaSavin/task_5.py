#! /usr/bin/env python
# TODO: A singleton is a class that allows only a single instance of itself to
# be created and gives access to that created instance. Implement singleton
# logic inside your custom class using a method to initialize class instance.


"""
task_5.py: implemented class Sun which allows only a single instance and some
tests stetements.
"""


class Sun:
    """
    Sun: singleton is a class that allows only a single instance of itself to
    be created and gives access to that created instance.
    """
    __instance = None

    def __init__(self):
        if Sun.__instance is not None:
            raise NotImplementedError('Cannot be created by constuctor')

    @classmethod
    def inst(cls):
        if cls.__instance is None:
            cls.__instance = Sun()
        return cls.__instance


if __name__ == '__main__':
    p = Sun.inst()
    f = Sun.inst()
    # g = Sun()  # Result: NotImplementedError: Cannot be created by constuctor
    print(p is f)  # Result: True
