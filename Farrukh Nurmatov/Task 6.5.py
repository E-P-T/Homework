"""A singleton is a class that allows only a single instance of itself to be created and gives access
 to that created instance.
Implement singleton logic inside your custom class using a method to initialize class instance."""


class Sun(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Sun, cls).__new__(cls)
        return cls.instance


if __name__ == '__main__':
    p = Sun()
    f = Sun()
    print(p is f)
