class Bird:
    name = ''

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Bird base class"        
    
    def fly(self):
        print(f'{self.name} bird can fly') 
    
    def walk(self):
        print(f'{self.name} bird can walk') 
        
        
class FlyingBird(Bird):
    name = ''
    ration = ''
    
    def __init__(self, name, ration='grains'):
        self.name = name
        self.ration = ration
    
    def __str__(self):
        return f"{self.name} can walk and fly"
            
    def eat(self):
        print(f'It eats mostly {self.ration} to fly')
        
        
class NonFlyingBird(Bird):
    name = ''
    ration = ''
    
    def __init__(self, name, ration='fish'):
        self.name = name
        self.ration = ration

    def __str__(self):
        return f"{self.name} can walk and swim"        

    def fly(self):
        pass        
    
    def eat(self):
        print(f'It eats mostly {self.ration} to swim')    
        
    def swim(self):
        print(f'{self.name} bird can swim')              
        
class SuperBird(NonFlyingBird, FlyingBird):
    name = ''
    ration = ''
    
    def __init__(self, name, ration='fish'):
        self.name = name
        self.ration = ration     

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"         
            
        
        
b = Bird("Any")
b.walk()


p = NonFlyingBird("Penguin", "fish")
p.walk()
p.swim()
p.eat()
p.fly()

c = FlyingBird("Canary")
print( str(c) )
c.eat()

s = SuperBird("Gull")
print( str(s) )
s.eat()

print(SuperBird.__mro__)
