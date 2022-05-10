class Money:
    def __init__(self, value, currency="USD"):
        self.exchange_rate = {"EUR": 0.93,
                              "BYN": 2.1,
                              "USD": 1}
        self.value = value
        self.currency = currency
        self.convert()


    def convert(self):
        self.value *= self.exchange_rate[self.currency]

    def __add__(self, other):
        try:
            return self.value + other.value
        except:
            return self.value + other

    __radd__ = __add__

    def __mul__(self, other):
        try:
            return self.value * other.value
        except:
            return self.value * other
    __rmul__ = __mul__

    def __sub__(self, other):
        try:
            return self.value - other.value
        except:
            return self.value - other
    __rsub__ = __sub__

    def __truediv__(self, other):
        try:
            return self.value / other.value
        except:
            return self.value / other
    __rtruediv__ = __truediv__


x = Money(10, "BYN")
y = Money(11)
z = Money(12.34, "EUR")
print(f"result in 'USD': {z + 3.11 * x + y * 0.8}")
print(f"result in 'USD':{sum([x, y, z])}")

