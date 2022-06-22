# ### Task 6.7
# Implement class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions (comparison, division,
# multiplication, addition and subtraction).
# Tip: use class attribute exchange rate which is dictionary and stores information about exchange
# rates to your default currency:
# ```python
# exchange_rate = {
#     "EUR": 0.93,
#     "BYN": 2.1,
#     ...
# }
#
# Example:
# ```python
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
# ```
# Have a look at @functools.total_ordering

from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, value, currency='USD', exchange_rate=None):

        if exchange_rate is None:
            exchange_rate = {
                "USD": 1,
                "EUR": 0.9499,
                "BYN": 2.5421,
                "RUB": 55.1193,
                "UAH": 29.5487,
                "PLN": 4.3897,
                "JPY": 135.4641}

        self.value = value / exchange_rate[currency]
        self.currency = currency

    def __add__(self, number):
        self.value += number
        return round(self.value, 2)

    def __sub__(self, number):
        self.value -= number
        return round(self.value, 2)

    def __mul__(self, number):
        self.value *= number
        return round(self.value, 2)

    def __eq__(self, number):
        return self.value == number

    def __lt__(self, number):
        return self.value < number

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__

    print('Result in USD:')

# x = Money(10, "BYN")
# y = Money(11)
# z = Money(12.34, "EUR")
# print(z + 3.11 * x + y * 0.8)

lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s)

# not fully completed