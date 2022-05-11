# Task 6.6
# Implement a class Money to represent value and currency. You need to
# implement methods to use all basic arithmetics expressions (comparison,
# division, multiplication, addition and subtraction). Tip: use class attribute
# exchange rate which is dictionary and stores information about exchange rates to your default currency:
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
# print(s) #result in “EUR”
# >>123.45 EUR

class Money:
    currency_rate = {
        "EUR": 1,
        "USD": 0.8,
        "BYN": 3.11,
        "JPY": 0.01,
        "KGS": 0.01
    }

    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def get_amount_in_def_currency(self):
        return self.amount * self.currency_rate[self.currency]

    def __add__(self, x):
        return Money(self.get_amount_in_def_currency() + x.get_amount_in_def_currency())

    def __sub__(self, other):
        return Money(
            self.get_amount_in_def_currency() - other.get_amount_in_def_currency())

    def __eq__(self, other):
        return self.get_amount_in_def_currency() == other.get_amount_in_def_currency()

    def __mul__(self, other):
        return Money(
            self.get_amount_in_def_currency() * other
        )

    def __truediv__(self, other):
        return Money(
            self.get_amount_in_def_currency() / other
        )

    def __lt__(self, other):
        return self.get_amount_in_def_currency() < other.get_amount_in_def_currency()

    def __le__(self, other):
        return self.get_amount_in_def_currency() <= other.get_amount_in_def_currency()

    def __ne__(self, other):
        return self.get_amount_in_def_currency() != other.get_amount_in_def_currency()

    def __ge__(self, other):
        return self.get_amount_in_def_currency() >= other.get_amount_in_def_currency()

    def __gt__(self, other):
        return self.get_amount_in_def_currency() > other.get_amount_in_def_currency()

    def __str__(self):
        return str(self.amount) + ' ' + self.currency


a = Money(10)
b = Money(12, "BYN")
print(a + b)
print(a >= b)
print(a < b)
print(a == b)
