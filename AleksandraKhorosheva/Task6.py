### Task 4.6
'''Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:
```python
exchange_rate = {
    "EUR": 0.93,
    "BYN": 2.1,
    ...
}'''

from functools import total_ordering


class Money():

    def __init__(self, value, currency="USD"):
        self.__exchange_rate = {
            "EUR": 0.93,
            "USD": 1,
            "RUS": 70,
            "BYN": 2.52
        }
        self.value = value
        self.currency = currency
        self.converted = self.to_default_currency(value)

    def to_default_currency(self, value):
        return value / self.__exchange_rate[self.currency]

    def from_default_currency(self, value):
        return Money(value * self.__exchange_rate[self.currency], self.currency)

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.value + other, self.currency)
        return self.from_default_currency(self.converted + other.converted)

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.value * other, self.currency)
        raise ValueError()

    __rmul__ = __mul__

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.value - other, self.currency)
        return self.from_default_currency(self.converted - other.converted)

    __rsub__ = __sub__

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.value / other, self.currency)
        raise ValueError()

    def __eq__(self, other):
        return self.converted == other.converted

    def __lt__(self, other):
        return self.converted < other.converted

    def __gt__(self, other):
        return self.converted > other.converted

    def __str__(self):
        return f'{round(self.value, 2)} {self.currency}'


x = Money(10, "BYN")
y = Money(11)
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8)

lst = [Money(10, "BYN"), Money(11), Money(12.01, "USD")]
s = sum(lst)
print(s)
