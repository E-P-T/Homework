class Bird:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print( f'{self.name} can walk' )
    def fly(self):
        print( f'{self.name} can fly' )

class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration
    def eat(self):
        print( self.name + ' eat mostly ' + self.ration )
    def __str__(self):
        return f'{self.name} can walk and fly'

class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration
    def fly(self):
        raise AttributeError(self.name +  " object has no attribute " + "fly") 
    def eat(self):
        print( f'{self.name} eat mostly {self.ration}' )
    def __str__(self):
        return f'{self.name}  can walk and swim'

class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration="meat"):
        super().__init__(name, ration)
    def __str__(self):
        return f'{self.name}  can walk, swim and fly'

b = Bird("Any")
b.walk()

p = FlyingBird("Canary")
p.eat()
p.walk()
p.fly()
print(str(p))

r = NonFlyingBird("Penguin", "fish")
r.eat()
print(str(r))
#r.fly() #AttributeError

s = SuperBird("Gull")
print(str(s))
s.eat()
print(SuperBird.mro())





