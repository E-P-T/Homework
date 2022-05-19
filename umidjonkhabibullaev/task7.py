class Money:
    default_currency = "USD"
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.95,
        "JPY": 128.81,
        "UZS": 11130.57,
        "CAD": 1.28,
        "CNY": 6.76,
        "QAR": 3.66,
    }
    
    def __init__(self, amount, name = default_currency):
        self.amount = amount
        self.name = name
    
    def convert_to_usd(cls):
        amount = cls.amount / cls.exchange_rates[cls.name]
        return amount

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.amount + other, self.name)
        total_amount = (self.convert_to_usd() + other.convert_to_usd()) * self.exchange_rates[self.name]
        return Money(total_amount, self.name)
    
    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.amount * other, self.name)
        total_amount = (self.convert_to_usd() * other.convert_to_usd()) * self.exchange_rates[self.name]
        return Money(total_amount, self.name)
    
    __rmul__ = __mul__

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.amount - other, self.name)
        total_amount = (self.convert_to_usd() - other.convert_to_usd()) * self.exchange_rates[self.name]
        return Money(total_amount, self.name)
    
    __rsub__ = __sub__

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.amount / other, self.name)
        total_amount = (self.convert_to_usd() / other.convert_to_usd()) * self.exchange_rates[self.name]
        return Money(total_amount, self.name)

    def __str__(self):
        return str(round(self.amount, 2)) + " " + self.name


if __name__ == "__main__":
    z = Money(25, "EUR")
    x = Money(10)
    y = Money(330000, "UZS")
    # print(y + x)
    print(z + x + y)
    print(sum([x, y, z]))
    