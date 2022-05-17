"""Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions
(comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores
information about exchange rates to your default currency:"""
from functools import total_ordering


@total_ordering
class Money:
    exchange_rate = {
            "EUR": 0.93,
            "BYN": 2.1,
            "JPY": 2.5,
            "USD": 1.0,
            }

    def __init__(self, value, currency="USD"):
        self.value = value
        self.currency = currency
        self._dollar_value = value * self.exchange_rate.get(self.currency)

    def __eq__(self, other):
        return self._dollar_value == other._dollar_value

    def __lt__(self, other):
        return self.value < other._dollar_value

    def __add__(self, other):
        dollar_res = self._dollar_value + other._dollar_value
        res = dollar_res / self.exchange_rate.get(self.currency)
        return Money(res, self.currency)

    def __sub__(self, other):
        dollar_res = self._dollar_value - other
        res = dollar_res / self.exchange_rate.get(self.currency)
        return Money(res, self.currency)

    def __mul__(self, num):
        res = self.value * num
        return Money(res, self.currency)

    def __div__(self, num):
        res = self.value / num
        return Money(res, self.currency)

    def __str__(self):
        return f"{round(self.value, 2)} {self.currency}"

    def __radd__(self, other):
        dollar_res = other + self._dollar_value
        res = dollar_res / self.exchange_rate.get(self.currency)
        return Money(res, self.currency)

    __rmul__ = __mul__
    __rsub__ = __sub__


if __name__ == '__main__':
    x = Money(10, "BYN")
    y = Money(11)  # define your own default value, e.g. “USD”
    z = Money(12.34, "EUR")
    print(f"x = {x._dollar_value}")
    print(f"y = {y._dollar_value}")
    print(f"z = {z._dollar_value}")
    print(z == y)
    print(z > y)
    print(x < y)
    print(x + z)
    print(y + x)
    print(3.11 * x)
    print(z + 3.11 * x + y * 0.8)
    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    print(s)