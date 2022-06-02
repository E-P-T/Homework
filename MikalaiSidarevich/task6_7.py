# Task 6.7
# Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions
# (comparison, division, multiplication, addition and subtraction).
# Tip: use class attribute exchange rate which is dictionary and stores information
# about exchange rates to your default currency:

# exchange_rate = {
#     "EUR": 0.93,
#     "BYN": 2.1,
#     ...
# }

class Money:
    """Class represents money value and its currency."""

    exchange_rate = {
        "EUR": 0.96,
        "BYN": 2.58,
        "USD": 1,
        "JPY": 129.34
    }

    def __init__(self, value, currency="USD"):
        """
        Initialize money quantity with `value` and currency with `currency`.
        """
        self._value = value
        self._currency = currency

    @property
    def value(self):
        """Get money quantity."""
        return self._value

    @property
    def currency(self):
        """Get money currency"""
        return self._currency

    @staticmethod
    def convert(money, currency):
        """Convert `money` quantity to `currency` specified."""
        if isinstance(money, Money):
            src_rate = Money.exchange_rate[money.currency]
            dst_rate = Money.exchange_rate[currency]
            value = money.value / src_rate * dst_rate
        else:
            # Numeric value is returned as is
            value = money
        return Money(value, currency)

    def __lt__(self, other):
        other = Money.convert(other, self.currency)
        return self.value < other.value

    def __le__(self, other):
        other = Money.convert(other, self.currency)
        return self.value <= other.value

    def __eq__(self, other):
        other = Money.convert(other, self.currency)
        return self.value == other.value

    def __ne__(self, other):
        other = Money.convert(other, self.currency)
        return self.value != other.value

    def __ge__(self, other):
        other = Money.convert(other, self.currency)
        return self.value >= other.value

    def __gt__(self, other):
        other = Money.convert(other, self.currency)
        return self.value > other.value

    def __add__(self, other):
        other = Money.convert(other, self.currency)
        return Money(self.value + other.value, self.currency)

    __radd__ = __add__

    def __sub__(self, other):
        other = Money.convert(other, self.currency)
        return Money(self.value - other.value, self.currency)

    __rsub__ = __sub__

    def __mul__(self, factor):
        return Money(self._value * factor, self._currency)

    __rmul__ = __mul__

    def __truediv__(self, factor):
        return Money(self._value / factor, self._currency)

    def __str__(self):
        return f"{self._value:.2f} {self._currency}"


def main():
    """
    Entry point function.
    """
    x = Money(10, "BYN")
    y = Money(11)  # define your own default value, e.g. “USD”
    z = Money(12.34, "EUR")
    print(z + 3.11 * x + y * 0.8)  # result in “EUR”

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    print(s)  # result in “BYN”

    print(f"{x} + 3.11 * {y} - 2 * {z} / 0.8 = {x + 3.11 * y - 2 * z / 0.8}")

    print(f"{x} < {y} is {x < y}")
    print(f"{x} <= {y} is {x <= y}")
    print(f"{x} == {y} is {x == y}")
    print(f"{x} != {y} is {x != y}")
    print(f"{x} >= {y} is {x >= y}")
    print(f"{x} > {y} is {x > y}")


if __name__ == '__main__':
    main()
