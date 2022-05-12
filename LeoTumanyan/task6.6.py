# ### Task 6.6

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
from functools import total_ordering


@total_ordering
class Money:
    rate = {
        "EUR": 480.24,
        "BYN": 139.191,
        "RUB": 7.02,
        "USD": 460.13
    }

    def __init__(self, val, cur="USD"):
        self.val = val
        self.cur = cur

    def conv_usd(self):
        return self.val / self.rate[self.cur]

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.val + other, self.cur)
        return Money((self.conv_usd() + other.conv_usd()) * self.rate[self.cur], self.cur)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.val * other, self.cur)
        else:
            return Money((self.conv_usd() * other.conv_usd()) * self.rate[self.cur], self.cur)

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
        return str(round(self.val, 2)) + " " + self.cur

    @classmethod
    def change_rate(cls, new_rate, new_cur):
        cls.rate[new_cur] = new_rate

    __radd__ = __add__
    __rmul__ = __mul__
