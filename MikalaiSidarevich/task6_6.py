# Task 6.6
# A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.

class Sun:
    """The sun exists in a single copy."""

    _instance = None

    def __new__(cls):
        """
        Create a new instance of class `cls`.
        """
        if not cls._instance:
            cls._instance = object.__new__(cls)

    @classmethod
    def inst(cls):
        """
        Get an instance of the class.
        """
        return cls._instance


def main():
    """
    Entry point function.
    """
    a = Sun()
    b = Sun()
    print(a is b)

    p = Sun.inst()
    f = Sun.inst()
    print(p is f)


if __name__ == '__main__':
    main()
