class Base:
    def __init__(self):
        self.a = 'base object'

class Sun:
    obj = Base()

    @classmethod
    def inst(self):
        return self.obj


p = Sun.inst()
f = Sun.inst()

print(p is f)
