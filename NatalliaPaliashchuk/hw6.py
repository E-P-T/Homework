# # Python Practice - Session 4


# ### Task 4.1
# Implement a Counter class which optionally accepts the start value and the counter stop value.
# If the start value is not specified the counter should begin with 0.
# If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached."

# Implement to methods: "increment" and "get"

# * <em>If you are familiar with Exception rising use it to display the "Maximal value is reached." message.</em>

# Example:
# ```python
# >>> c = Counter(start=42)
# >>> c.increment()
# >>> c.get()
# 43

# >>> c = Counter()
# >>> c.increment()
# >>> c.get()
# 1
# >>> c.increment()
# >>> c.get()
# 2

# >>> c = Counter(start=42, stop=43)
# >>> c.increment()
# >>> c.get()
# 43
# >>> c.increment()
# Maximal value is reached.
# >>> c.get()
# 43
# ```
class Counter:
    def __init__(self, start=0, stop=None):
        self.start = start
        self.stop = stop
        
    def increment(self):
        if self.stop is not None and self.start >= self.stop:
            print('Maximal value is reached')
        else:
            self.start += 1
            
    def get(self): return self.start

# #### Task 4.2
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.


# Example:
# ```python
# >>> d = HistoryDict({"foo": 42}) 
# >>> d.set_value("bar", 43)
# >>> d.get_history()

# ["bar"]
# ```

# <em>After your own implementation of the class have a look at collections.deque https://docs.python.org/3/library/collections.html#collections.deque </em>
class HistoryDict:
    def __init__(self, dict_):
        if isinstance(dict_, dict):
            self.dict = dict_
            self.keys = []
        else:
            raise TypeError('Dict type is expected')
    
    def set_value(self, key, value):
        if key in self.keys:
            pass
        elif len(self.keys) < 10:
            self.keys.append(key)
        else:
            del self.keys[0]
            self.keys.append(key)
        self.dict[key] = value
        
    def get_history(self): return self.keys[::-1]
        
    

# ### Task 4.3
# Implement The Keyword encoding and decoding for latin alphabet.
# The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
# Add the provided keyword at the begining of the alphabet.
# A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet. 
# Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

# <em> Encryption:
# Keyword is "Crypto"

# * A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# * C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
# </em>

# Example:
# ```python
# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"

# >>> cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"
# ```
from string import ascii_uppercase

class Cipher:
    def __init__(self, keyword):
        keyword = keyword.upper()
        for letter in ascii_uppercase:
            if letter not in keyword:
                keyword = keyword + letter                
        self.table = str.maketrans(ascii_uppercase+ascii_uppercase.lower(), keyword+keyword.lower())
        self.table_decod = str.maketrans(keyword+keyword.lower(), ascii_uppercase+ascii_uppercase.lower())
    
    def encode(self, str_):
        return str_.translate(self.table)
    
    def decode(self, str_):
        return str_.translate(self.table_decod)
    
    

# ### Task 4.4
# Create hierarchy out of birds. 
# Implement 4 classes:
# * class `Bird` with an attribute `name` and methods `fly` and `walk`.
# * class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value. 
# Implement the method `eat` which will describe its typical ration.
# * class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
# Add same "eat" method but with other implementation regarding the swimming bird tastes.
# * class `SuperBird` which can do all of it: walk, fly, swim and eat.
# But be careful which "eat" method you inherit.

# Implement str() function call for each class.

# Example:
# ```python
# >>> b = Bird("Any")
# >>> b.walk()
# "Any bird can walk"

# p = NonFlyingBird("Penguin", "fish")
# >> p.swim()
# "Penguin bird can swim"
# >>> p.fly()
# AttributeError: 'Penguin' object has no attribute 'fly'
# >>> p.eat()
# "It eats mostly fish"

# c = FlyingBird("Canary")
# >>> str(c)
# "Canary can walk and fly"
# >>> c.eat()
# "It eats mostly grains"

# s = SuperBird("Gull")
# >>> str(s)
# "Gull bird can walk, swim and fly"
# >>> s.eat()
# "It eats fish"
# ```

# Have a look at __mro__ method of your last class.
class Bird:
    def __init__(self, name): self.name = name
    
    def fly(self): return f"{self.name} bird can fly"
        
    def walk(self): return "Any bird can walk"

class FlyingBird(Bird):
    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def eat(self): return f"It eats mostly {self.ration}"
    
    def __str__(self): return f"{self.name} can walk and fly"
    
class NonFlyingBird(FlyingBird):
    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.ration = ration
    
    def swim(self): return f"{self.name} bird can swim"
    
    def fly(self): raise AttributeError(f"{self.name} object has no attribute 'fly'")
        
    
class SuperBird(NonFlyingBird, FlyingBird,):
    def __str__(self): return f"{self.name} can walk, swim and fly"


# ### Task 4.6

# A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance. 
# Implement singleton logic inside your custom class using a method to initialize class instance.

# Example:

# ```python
# >>> p = Sun.inst()
# >>> f = Sun.inst()
# >>> p is f
# True
# ```
class Sun:
    count = 0
   
    @classmethod    
    def inst(cls):
        if cls.count == 0:
           cls.result = cls()
           cls.count += 1
           return cls.result
        else:
           return cls.result

# ### Task 4.7 
# Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
# Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:
# ```python
# exchange_rate = {
#     "EUR": 0.93,
#     "BYN": 2.1,
#     ...
# }
# ```

# Example:
# ```python
# x = Money(10, "BYN")
# y = Money(11) # define your own default value, e.g. “USD”
# z = Money(12.34, "EUR")
# print(z + 3.11 * x + y * 0.8) # result in “EUR”
# >>543.21 EUR

# lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
# s = sum(lst)
# print(s) #result in “BYN”
# >>123.45 BYN
# ```

# <em>Have a look at @functools.total_ordering</em>

class Money:
    exchange_rate = {'EUR': 0.93, 'BYN': 2.1, 'USD': 1, 'JPY': 100}
    
    def __init__(self, value, currency='USD'):
        self.value, self.currency = value, currency
     
    def __add__(self, obj):
        if not isinstance(obj, Money):
            result =  obj + self.value
        else:
            result = self.value + obj.value / Money.exchange_rate[obj.currency] * Money.exchange_rate[self.currency]
        return Money(result, self.currency)
    
    __radd__ = __add__
    
    def __sub__(self, obj):
        if not isinstance(obj, Money):
            result = self.value - obj 
        else:
            result = self.value - obj.value / Money.exchange_rate[obj.currency] * Money.exchange_rate[self.currency]
        return Money(result, self.currency)
    
    def __rsub__(self, obj): return Money(obj - self.value, self.currency)
    
    def __mul__(self, obj):
        if not isinstance(obj, Money):
            result = self.value * obj 
        else:
            result = self.value * obj.value / Money.exchange_rate[obj.currency] * Money.exchange_rate[self.currency]
        return Money(result, self.currency)
    
    __rmul__ = __mul__
    
    def __truediv__(self, obj):
        if not isinstance(obj, Money):
            result = self.value / obj 
        else:
            result = self.value / (obj.value / Money.exchange_rate[obj.currency] * Money.exchange_rate[self.currency])
        return Money(result, self.currency)
    
    def __rtruediv__(self, obj): return Money(obj/self.value, self.currency)
        
    def __eq__(self, obj): return  self.value / Money.exchange_rate[self.currency] == obj.value / Money.exchange_rate[obj.currency]
    
    def __lt__(self, obj): return self.value / Money.exchange_rate[self.currency] < obj.value / Money.exchange_rate[obj.currency]
            
    def __str__(self): return f'{self.value} {self.currency}' 

# ### Task 4.8

# Implement a Pagination class helpful to arrange text on pages and list content on given page. 
# The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page (take spaces into account as well).
# You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that accepts the page number and return quantity of symbols on this page.
# If the provided number of the page is missing print the warning message "Invalid index. Page is missing". If you're familliar with using of Excpetions in Python display the error message in this way.
# Pages indexing starts with 0.

# Example:
# ```python
# >>> pages = Pagination('Your beautiful text', 5)
# >>> pages.page_count
# 4
# >>> pages.item_count
# 19

# >>> pages.count_items_on_page(0)
# 5
# >>> pages.count_items_on_page(3)
# 4
# >>> pages.count_items_on_page(4)
# Exception: Invalid index. Page is missing.
# ```
# Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it.
# If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in two return an array of all the occurences.

# Example:
# ```python
# >>> pages.find_page('Your')
# [0]
# >>> pages.find_page('e')
# [1, 3]
# >>> pages.find_page('beautiful')
# [1, 2]
# >>> pages.find_page('great')
# Exception: 'great' is missing on the pages
# >>> pages.display_page(0)
# 'Your '
# ```
from math import ceil

class Pagination:
    def __init__(self, txt, smbl):
        self.text, self.smbl = txt, smbl
        self.item_count = len(self.text)
        self.page_count = ceil(self.item_count / self.smbl)
    
    def count_items_on_page(self, nmbr):
        if 0 <= nmbr < self.page_count - 1:
            return self.smbl
        elif nmbr == self.page_count - 1:
            return self.item_count % self.smbl
        else:
            raise Exception('Invalid index. Page is missing')
    
    def display_page(self, page):
        return self.text[self.smbl * page : self.smbl * (page + 1)]
    
    def find_page(self, word):
        result = []
        for page in range(self.page_count):
            if word in self.display_page(page):
                result.append(page)
        if result: return result
        else: raise Exception('Invalid index. Page is missing.')