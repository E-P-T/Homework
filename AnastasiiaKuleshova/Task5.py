# Task 6.5
# A singleton is a class that allows only a single instance of itself to
# be created and gives access to that created instance. Implement singleton l
# ogic inside your custom class using a method to initialize class instance.
#
# Example:
#
# >>> p = Sun.inst(
# >>> f = Sun.inst()
# >>> p is f
# True

class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class Sun(Singleton):
    @staticmethod
    def inst():
        return Sun()


d = Sun.inst()
c = Sun.inst()
print(d is c)
