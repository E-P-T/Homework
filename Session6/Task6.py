"""
Implement a class Money to represent value and currency. You need to implement methods to use all
basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information about
exchange rates to your default currency:
"""

class Money:
    exchange_rate = {
        "AMD": 1,
        "USD": 450,
        "RUB": 6.5,
        "EUR": 500,
        "GBP": 550
    }

    def __init__(self, value, currency="AMD"):
        self.value = value
        self.currency = currency

    def to_amd_convert (self):
        return self.value / self.exchange_rate[self.currency]

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.value + other, self.currency)
        return Money((self.to_amd_convert () + other.to_amd_convert ()) * self.exchange_rate[self.currency], self.currency)

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.value * other, self.currency)
        else:
            return Money((self.to_amd_convert() * other.to_amd_convert()) * self.exchange_rate[self.exchange_rate],self.currency)

    __rmul__=__mul__

    def __sub__(self, other):
        return Money((self.to_amd_convert() - other.to_amd_convert()) * self.exchange_rate[self.exchange_rate],self.currency)

    __rsub__=__sub__

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.value / self.currency)
        else:
            return Money((self.to_amd_convert() / other.to_amd_convert)* self.exchange_rate[self.exchange_rate],self.currency)

    def __eq__(self, other):
        return self.to_amd_convert == other.to_amd_convert

    def __lt__(self, other):
        return self.to_amd_convert < other.to_amd_convert

    def __str__(self):
        return str(round(self.value, 2)) + " " + self.currency
"""
x = Money(10, "USD")
y = Money(11)
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8)
"""
lst = [Money(10,"EUR"), Money(11), Money(12.01, "USD")]
s = sum(lst)
print(s) #result in “BYN”
