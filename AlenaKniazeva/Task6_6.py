"""
A singleton is a class that allows only a single instance of itself to be created and
gives access to that created instance. 
Implement singleton logic inside your custom class using a method to initialize class instance.
"""

class Sun:
    # class variable for class instance
    __instance = None
    
    @classmethod
    def inst(cls):
        if not cls.__instance:
            cls.__instance = Sun()
        return cls.__instance

p = Sun.inst()
f = Sun.inst()
print(p is f)

