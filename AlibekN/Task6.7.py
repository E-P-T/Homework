from functools import total_ordering


@total_ordering
class Money:
    rate = {
        "EUR": 0.93,
        "BYN": 2.1,
        "USD": 1,
    }
    def __init__(self, amount, curr="USD"):
        self.amount = amount
        self.curr = curr

    def get_currency(self):
        return self.amount * self.rate[self.curr]

    def __add__(self, other):
        return Money( (self.get_currency() + other.get_currency()), self.curr)
    def __sub__(self, other):
        return Money( (self.get_currency() - other.get_currency()), self.curr)
    def __mul__(self, value):
        return Money( (self.amount * self.rate[self.curr] * value), self.curr )
    __rmul__ = __mul__
   

    def __lt__(self, other):
        return self.amount < other.amount
    
    def __str__(self):
        return str(self.amount) + " " + str(self.curr)

x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")

print(y * 0.8 )
print(z + 3.11 * x + y * 0.8)


