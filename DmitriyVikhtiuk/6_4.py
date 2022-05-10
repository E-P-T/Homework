class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} bird can fly")
    def walk(self):
        print(f"{self.name} bird can walk")

class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        self.name = name
        self.food = ration
        super().__init__(name)

    def eat(self):
        print(f"It eats mostly {self.food}")

    def __str__(self):
        return f"{self.name} can walk and fly"

class NonFlyingBird(FlyingBird):
    def __init__(self, name, ration):
        super().__init__(name, ration)
    def fly(self):
        raise AttributeError(f"'{self.name}' object has no attribute 'fly'")
    def swim(self):
        print(f"{self.name} bird can swim")
    def eat(self):
        super().eat()
    def __str__(self):
        return f"{self.name} can walk and swim"



class SuperBird(NonFlyingBird):
    def __init__(self, name, ration="fish"):
        super().__init__(name, ration)
    def fly(self):
        print(f"{self.name} bird can fly")
    def  __str__(self):
        return f"{self.name} can walk, swim and fly"

    def eat(self):
        print(f"It eats {self.food}")



b = Bird("Any")
b.walk()
c = FlyingBird("Canary")
str(c)
c.eat()
p = NonFlyingBird("Penguin", "fish")
p.swim()
p.eat()
str(p)
p.fly()
s = SuperBird("Gull")
s.eat()
str(s)
print(SuperBird.__mro__)
