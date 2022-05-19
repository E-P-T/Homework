### First Approach: Using custom classmethod ###
class President:
    __instance = None # class variable representing the whether a class has instance
    @classmethod
    def inst(cls):
        if not cls.__instance:
            cls.__instance = President()
        print(cls.__instance)
        return cls.__instance

real_president = President.inst()
fake_president = President.inst()
print(fake_president is real_president)


# ================================================================================= #


### Second Approach: Using magic method __new__ ###
class Passport:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(Passport, cls).__new__(cls)
        return cls.instance

my_passport = Passport("AB1010101")
another_passort = Passport("AC0101010")
print(another_passort is my_passport)