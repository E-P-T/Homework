class Money:
    _exchange_rate = {
        'EUR': 0.93,
        'BYN': 2.0,
        'USD': 1,
        "JPY": 2.0
    }

    def __init__(self, value, currency='USD'):
        self.value = value
        self.currency = currency
        self.default_currency = self.convert_to_def_cur(self.value)

    def convert_to_def_cur(self, value):
        return value / self._exchange_rate[self.currency]

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.default_currency + other)
        return Money(self.default_currency + other.default_currency)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.default_currency - other)
        return Money(self.default_currency - other.default_currency)

    __rsub__ = __sub__

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.default_currency * other)
        raise ValueError()

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.default_currency / other)
        raise ValueError()

    __rtruediv__ = __truediv__

    def __str__(self):
        return f'{self.value} USD'


if __name__ == '__main__':

    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")
    print(z + 3.11 * x + y * 0.8)

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "USD")]
    s = sum(lst)
    print(s)

