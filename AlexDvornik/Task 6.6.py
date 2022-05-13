"""
Task 6.6
Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:

exchange_rate = {
    "EUR": 0.93,
    "BYN": 2.1,
    ...
}

"""

from functools import total_ordering


@total_ordering
class Money:
    def __init__(self, value, currency='USD'):
        self.value = value
        self.currency = currency
        self.__exchange_rate = {
            "EUR": 0.93,
            "BYN": 2.1,
            "USD": 1,
            "RUS": 69.17,
        }
        self.converted = self.get_converted()

    @property
    def exchange_rate(self):
        return self.__exchange_rate

    def get_converted(self):
        return self.value / self.__exchange_rate[self.currency]

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.value + other, self.currency)
        return Money((self.converted + other.converted) * self.exchange_rate[self.currency], self.currency)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.value * other, self.currency)
        return Money((self.converted * other.converted) * self.exchange_rate[self.currency], self.currency)

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.value - other, self.currency)
        return Money((self.converted - other.converted) * self.exchange_rate[self.currency], self.currency)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            try:
                return Money(self.value / other, self.currency)
            except ZeroDivisionError as error:
                print(error)
        else:
            try:
                return Money((self.converted / other.converted) * self.exchange_rate[self.currency], self.currency)
            except ZeroDivisionError as error:
                print(error)

    def __eq__(self, other):
        return self.converted == other.converted

    def __lt__(self, other):
        return self.converted < other.converted

    def __gt__(self, other):
        return self.converted > other.converted

    def __str__(self):
        return f" {round(self.value, 2)} {self.currency}"


x = Money(10, "BYN")
y = Money(12.34, "EUR")
z = Money(11)
print(x + y + z)

lst = [Money(10, "BYN"), Money(11), Money(12.01, "RUS")]
print(sum(lst))

print(y + x)
print(y * x)
print(y / x)
print(y > x)

