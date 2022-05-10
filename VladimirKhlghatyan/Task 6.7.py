# Task 6.7
# Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetic expressions
# (comparison, division, multiplication, addition and subtraction).
# Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates
# to your default currency:
#
# exchange_rate = {
#     "EUR": 0.93,
#     "BYN": 2.1,
#     ...
# }
# Example:
#
# x = Money(10, "BYN")
# y = Money(11) # define your own default value, e.g. “USD”
# z = Money(12.34, "EUR")
# print(z + 3.11 * x + y * 0.8) # result in “EUR”
# >>543.21 EUR
#
# lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
# s = sum(lst)
# print(s) #result in “BYN”
# >>123.45 BYN
# Have a look at @functools.total_ordering


class Money:
    exchange_rate = {
        "AMD": 1.0,
        "USD": 470.3,
        "EUR": 500.5,
        "RUB": 6.5,
    }

    def __init__(self, value, currency="AMD"):
        self.value = value
        self._currency = currency

    def __str__(self):
        return '{} : {}'.format(self._currency, self.value)

    def get_value(self):
        return self.value

    def get_currency(self):
        return self._currency

    def convert(self, other):
        return self.get_value() * self.exchange_rate[other.get_currency()] / self.exchange_rate[self.get_currency()]

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.get_value() == other.convert(self)
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_value() == other

    def __ne__(self, other):
        if isinstance(other, Money):
            return self.get_value() != other.convert(self)
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_value() != other

    def __gt__(self, other):
        if isinstance(other, Money):
            return self.get_value() > other.convert(self)
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_value() > other

    def __ge__(self, other):
        if isinstance(other, Money):
            return self.get_value() >= other.convert(self)
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_value() >= other

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.get_value() < other.convert(self)
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_value() < other

    def __le__(self, other):
        if isinstance(other, Money):
            return self.get_value() <= other.convert(self)
        elif isinstance(other, int) or isinstance(other, float):
            return self.get_value() <= other

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.get_value() + other.convert(self), self.get_currency())
        elif isinstance(other, int) or isinstance(other, float):
            return Money(self.get_value() + other, self.get_currency())

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self.get_value() - other.convert(self), self.get_currency())
        elif isinstance(other, int) or isinstance(other, float):
            return Money(self.get_value() - other, self.get_currency())

    def __mul__(self, other):
        if isinstance(other, Money):
            return Money(self.get_value() * other.convert(self), self.get_currency())
        elif isinstance(other, int) or isinstance(other, float):
            return Money(self.get_value() * other, self.get_currency())

    def __truediv__(self, other):
        if isinstance(other, Money):
            return Money(self.get_value() / other.convert(self), self.get_currency())
        elif isinstance(other, int) or isinstance(other, float):
            return Money(self.get_value() / other, self.get_currency())

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rtruediv__ = __truediv__
