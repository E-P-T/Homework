class Bird:
    def __init__(self, name):
        self.name = name
    
    def fly(self):
        return f"{self.name} bird can fly"

    def walk(self):
        return f"{self.name} bird can walk"
    
    def __str__(self) -> str:
        available_methods = [method for method in dir(self) if not method.startswith("__") and method not in list(self.__dict__.keys())]
        return_str = f"{self.name} bird can "
        for method in available_methods:
            if method == available_methods[-1]:
                return_str += f"and {method}"
                continue
            return_str += f"{method}, "
        return return_str


class FlyingBird(Bird):
    def __init__(self, name, ration = "grains"):
        self.name = name
        self.ration = ration
    
    def eat(self):
        return f"{self.name} bird mostly eats {self.ration}"
    
    def __str__(self) -> str:
        return super().__str__()


class NonFlyingBird(FlyingBird):
    def __init__(self, name, ration="fish"):
        super().__init__(name, ration)
    
    def fly(self):
        raise AttributeError (f"'{self.__class__.__name__}' object has no attribute 'fly'")
    
    def swim(self):
        return f"{self.name} bird can swim"

    def __str__(self) -> str:
        return super().__str__().replace("fly, ", "")


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name, ration="anything"):
        super().__init__(name, ration)
    
    def fly(self):
        return super(FlyingBird, self).fly()
    
    def __str__(self) -> str:
        return super(FlyingBird, self).__str__()


muchicha = FlyingBird("Muchicha", "insects")
print(muchicha.fly())
print(muchicha.walk())
print(muchicha.eat())
print(muchicha)
print("=" * 120)

penguin = NonFlyingBird("Penguin", "fish")
print(penguin.eat())
print(penguin.swim())
# print(penguin.fly())
print(penguin)
print("=" * 120)

gull = SuperBird("Gull")
print(gull.eat())
print(gull.fly())
print(gull.swim())
print(SuperBird.mro())