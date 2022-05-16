#Singleton 
class Sun(object):
    obj = None 
    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *args, **kwargs)
        if cls.obk is None:
            cls.obj = object.__new__(cls, *args, **kwargs)
        return cls.obj

p = Sun()
f = Sun()

print(p is f)