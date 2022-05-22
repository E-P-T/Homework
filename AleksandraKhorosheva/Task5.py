### Task 4.5

'''A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance.
Implement singleton logic inside your custom class using a method to initialize class instance.
'''

class Sun():

    _instance = None

    def __init__(self):
        pass

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = super(Sun, cls).__new__(cls)
        return cls._instance


p = Sun.inst()
f = Sun.inst()
print(p is f)
