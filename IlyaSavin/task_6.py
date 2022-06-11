#! /usr/bin/env python
# TODO: Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions
# (comparison, division, multiplication, addition and subtraction).
# Tip: use class attribute exchange rate which is dictionary and stores
# information about exchange rates to your default currency:


"""
task_6.py: Implemented a class Money to represent value and currency.
Also contains some test statements for this class.
"""


class Money:
    """
    Money: represent value and currency of money. Class supports
    converting between currencies and simple arithmetics operations.
    """
    rate = {
        'USD': 1.0,
        'EUR': 0.93,
        'BYN': 3.38,
        'JPY': 130.84
    }

    def __init__(self, amount, currency='USD'):
        self.amount = amount
        self.currency = currency

    @staticmethod
    def convert(money, currency):
        return money.amount / Money.rate[money.currency] * Money.rate[currency]

    def __add__(self, money):
        if isinstance(money, Money):
            converted_money = Money.convert(money, self.currency)
            return Money(self.amount + converted_money, currency=self.currency)
        else:
            return Money(self.amount + money, currency=self.currency)

    def __mul__(self, money):
        if isinstance(money, Money):
            converted_money = Money.convert(money, self.currency)
            return Money(self.amount * converted_money, currency=self.currency)
        else:
            return Money(self.amount * money, currency=self.currency)

    def __sub__(self, money):
        if isinstance(money, Money):
            converted_money = Money.convert(money, self.currency)
            return Money(self.amount - converted_money, currency=self.currency)
        else:
            return Money(self.amount - money, currency=self.currency)

    def __truediv__(self, money):
        if isinstance(money, Money):
            converted_money = Money.convert(money, self.currency)
            return Money(self.amount / converted_money, currency=self.currency)
        else:
            return Money(self.amount / money, currency=self.currency)

    def __eq__(self, money):
        if isinstance(money, Money):
            return self.amount == Money.convert(money, self.currency)
        else:
            return self.amount == money

    def __ne__(self, money):
        return not self == money

    def __lt__(self, money):
        if isinstance(money, Money):
            return self.amount < Money.convert(money, self.currency)
        else:
            return self.amount < money

    def __gt__(self, money):
        return not self < money

    def __le__(self, money):
        if isinstance(money, Money):
            return self.amount <= Money.convert(money, self.currency)
        else:
            return self.amount <= money

    def __ge__(self, money):
        return not self <= money

    def __str__(self):
        return f'{round(self.amount, 2)} {self.currency}'

    __radd__ = __add__
    __rmul__ = __mul__
    __rsub__ = __sub__
    __rtruediv = __truediv__


if __name__ == '__main__':
    x = Money(10, 'BYN')
    y = Money(11)
    z = Money(12.34, 'EUR')
    print(z + 3.11 * x + y * 0.8)  # Result: 29.08 EUR

    lst = [Money(10, 'BYN'), Money(11), Money(12.01, 'JPY')]
    s = sum(lst)
    print(s)  # Result: 47.49 BYN

    w = z - x * y / s
    print(w)  # Result: 10.19 EUR

    print(x < y)  # Result: True
    print(y > x)  # Result: True
    print(x == y)  # Result: False
    print(x != y)  # Result: True
    print(x <= y)  # Result: True
    print(y >= x)  # Result: True
    print(x < 9)  # Result: False
    print(y > 10)  # Result: True
    print(x == 5.5)  # Result: False
    print(x != 5.5)  # Result: True
    print(x <= 9)  # Result: False
    print(y >= 10)  # Result: True
