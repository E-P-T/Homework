"""
Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions
(comparison, division, multiplication, addition and subtraction).
"""

from functools import total_ordering

@total_ordering
class Money:
    rate = {
    "EUR": 0.4,
    "BYN": 2.1,
    "RUB": 69.17,
    "USD": 1
    }

    def __init__(self, val, cur = "USD"):
        self.val = val
        self.cur = cur

    def conv_usd (self):
        return self.val / self.rate[self.cur]

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.val + other, self.cur)
        return Money((self.conv_usd() + other.conv_usd()) * self.rate[self.cur], self.cur)

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.val * other, self.cur)
        else:
            return Money((self.conv_usd() * other.conv_usd()) * self.rate[self.cur], self.cur)

    __rmul__ = __mul__

    def __sub__(self, other):
        return Money((self.conv_usd() - other.conv_usd()) * self.rate[self.cur], self.cur)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.val / other, self.cur)
        else:
            return Money((self.conv_usd() / other.conv_usd()) * self.rate[self.cur], self.cur)

    def __eq__(self, other):
        return self.conv_usd() == other.conv_usd()

    def __lt__(self, other):
        return self.conv_usd() < other.conv_usd()

    def __str__(self):
        return str(round(self.val,2)) + " " + self.cur

    # function to update exchange rates
    @ classmethod
    def change_rate (cls, new_rate, new_cur):
        cls.rate[new_cur] = new_rate


x = Money(10, "BYN")
y = Money(11)
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8)

a = Money(10, "EUR")
b = Money(11, "RUB") 
print(a > b)
print(a != b)

lst = [Money(10, "BYN"), Money(11), Money(12.34, "EUR")]
print(x + y + z)
s = sum(lst)
print(s) #result in “BYN”

Money.change_rate(10,"LTV")
print(Money.rate)
