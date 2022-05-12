# ### Task 6.5

# A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.

# Example:

class Sun:
    __instance = None

    def __init__(self):
        pass

    @classmethod
    def inst(cls):
        if cls.__instance is None:
            cls._instance = super(Sun, cls).__new__(cls)
        return cls.__instance


p = Sun.inst()
f = Sun.inst()
print(p is f)
