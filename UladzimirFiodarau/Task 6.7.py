# Task 4.7
# Implement a class Money to represent value and currency. You need to implement methods to use all basic arithmetics
# expressions (comparison, division, multiplication, addition and subtraction). Tip: use class attribute exchange rate
# which is dictionary and stores information about exchange rates to your default currency:
#
# Have a look at @functools.total_ordering

class Money(object):
    exchange_rate = {
        "EUR": 0.9512,
        "BYN": 2.6534,
        "USD": 1,
        "RUB": 72.3115,
        "UAH": 30.2499,
        "PLN": 4.4621
    }

    def __init__(self, value, currency):
        self._value = value
        self._currency = currency

    def __str__(self):
        return f'{self._value} {self._currency}'

    def __repr__(self):
        return Money({self._value}, {self._currency})

    def get_value(self):
        return self._value

    def get_curr(self):
        return self._currency

    def convert(self, other):
        return round(self._value * self.exchange_rate[other.get_curr()] / self.exchange_rate[self.get_curr()], 4)

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(round(self._value + other.convert(self), 4), self._currency)
        elif isinstance(other, int) or isinstance(other, float):
            return Money(round(self._value + other, 4), self._currency)

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(round(self._value - other.convert(self), 4), self._currency)
        elif isinstance(other, int) or isinstance(other, float):
            return Money(round(self._value - other, 4), self._currency)

    def __mul__(self, other):
        if isinstance(other, Money):
            return Money(round(self._value * other.convert(self), 4), self._currency)
        elif isinstance(other, int) or isinstance(other, float):
            return Money(round(self._value * other, 4), self._currency)

    def __truediv__(self, other):
        if isinstance(other, Money):
            return Money(round(self._value / other.convert(self), 4), self._currency)
        elif isinstance(other, int) or isinstance(other, float):
            return Money(round(self._value / other, 4), self._currency)

    def __eq__(self, other):
        if isinstance(other, Money):
            return round(self._value, 4) == round(other.convert(self), 4)
        elif isinstance(other, int) or isinstance(other, float):
            return round(self._value, 4) == round(other, 4)

    def __eq__(self, other):
        if isinstance(other, Money):
            return round(self._value, 4) == round(other.convert(self), 4)
        elif isinstance(other, int) or isinstance(other, float):
            return round(self._value, 4) == round(other, 4)

    def __ne__(self, other):
        if isinstance(other, Money):
            return round(self._value, 4) != round(other.convert(self), 4)
        elif isinstance(other, int) or isinstance(other, float):
            return round(self._value, 4) != round(other, 4)

    def __gt__(self, other):
        if isinstance(other, Money):
            return round(self._value, 4) > round(other.convert(self), 4)
        elif isinstance(other, int) or isinstance(other, float):
            return round(self._value, 4) > round(other, 4)

    def __ge__(self, other):
        if isinstance(other, Money):
            return round(self._value, 4) >= round(other.convert(self), 4)
        elif isinstance(other, int) or isinstance(other, float):
            return round(self._value, 4) >= round(other, 4)

    def __lt__(self, other):
        if isinstance(other, Money):
            return round(self._value, 4) < round(other.convert(self), 4)
        elif isinstance(other, int) or isinstance(other, float):
            return round(self._value, 4) < round(other, 4)

    def __le__(self, other):
        if isinstance(other, Money):
            return round(self._value, 4) <= round(other.convert(self), 4)
        elif isinstance(other, int) or isinstance(other, float):
            return round(self._value, 4) <= round(other, 4)


    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rtruediv__ = __truediv__


# x = Money(10, "BYN")
# y = Money(11, "USD")
# z = Money(12.34, "EUR")
# print(x)
# # 10 BYN
#
#
# print(x != y)
# # True
# p = Money(10, "BYN")
# print(x == p)
# # True
#
# print(y > z)
# # False
#
# print(x < y)
# # True
#
# print(z + 3.11 * x + y * 0.8) # result in “EUR”
# # 31.8594 EUR
#
# L = [x, y, z]
# s = sum(L)
# print(s)
# # 73.6102 BYN