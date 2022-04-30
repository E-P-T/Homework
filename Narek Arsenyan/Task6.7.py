class Money:
    exchange_rate = {
        "AMD": 1,
        "USD": 450,
        "RUB": 6.5,
        "EUR": 470,
        "GBP": 550,
        "AUD": 310
    }

    def __init__(self, value, currency="AMD"):
        self.value = value
        self.currency = currency

    def __str__(self):
        return "{0} {1}".format(self.value, self.currency)

    def __add__(self, other):
        rightValue = 0
        leftValue = self.exchange_rate[self.currency] * self.value
        if type(other) is int or type(other) is float:
            rightValue = other
        else:
            rightValue = self.exchange_rate[other.currency] * other.value

        finalValue = leftValue + rightValue
        return Money(finalValue / self.exchange_rate[self.currency], self.currency)

    def __sub__(self, other):
        rightValue = 0
        leftValue = self.exchange_rate[self.currency] * self.value
        if type(other) is int or type(other) is float:
            rightValue = other
        else:
            rightValue = self.exchange_rate[other.currency] * other.value

        finalValue = leftValue - rightValue
        return Money(finalValue / self.exchange_rate[self.currency], self.currency)

    def __mul__(self, other):
        rightValue = 0
        leftValue = self.exchange_rate[self.currency] * self.value
        if type(other) is int or type(other) is float:
            rightValue = other
        else:
            rightValue = self.exchange_rate[other.currency] * other.value

        finalValue = leftValue * rightValue
        return Money(finalValue / self.exchange_rate[self.currency], self.currency)

    def __truediv__(self, other):
        rightValue = 0
        leftValue = self.exchange_rate[self.currency] * self.value
        if type(other) is int or type(other) is float:
            rightValue = other
        else:
            rightValue = self.exchange_rate[other.currency] * other.value

        finalValue = leftValue / rightValue
        return Money(finalValue / self.exchange_rate[self.currency], self.currency)

    def __lt__(self, other):
        rightValue = 0
        leftValue = self.exchange_rate[self.currency] * self.value
        if type(other) is int or type(other) is float:
            rightValue = other
        else:
            rightValue = self.exchange_rate[other.currency] * other.value

        return leftValue < rightValue

    def __le__(self, other):
        rightValue = 0
        leftValue = self.exchange_rate[self.currency] * self.value
        if type(other) is int or type(other) is float:
            rightValue = other
        else:
            rightValue = self.exchange_rate[other.currency] * other.value

        return leftValue <= rightValue

    def __gt__(self, other):
        rightValue = 0
        leftValue = self.exchange_rate[self.currency] * self.value
        if type(other) is int or type(other) is float:
            rightValue = other
        else:
            rightValue = self.exchange_rate[other.currency] * other.value

        return leftValue > rightValue

    def __ge__(self, other):
        rightValue = 0
        leftValue = self.exchange_rate[self.currency] * self.value
        if type(other) is int or type(other) is float:
            rightValue = other
        else:
            rightValue = self.exchange_rate[other.currency] * other.value

        return leftValue >= rightValue

    def __eq__(self, other):
        rightValue = 0
        leftValue = self.exchange_rate[self.currency] * self.value
        if type(other) is int or type(other) is float:
            rightValue = other
        else:
            rightValue = self.exchange_rate[other.currency] * other.value

        return leftValue == rightValue

    def __ne__(self, other):
        rightValue = 0
        leftValue = self.exchange_rate[self.currency] * self.value
        if type(other) is int or type(other) is float:
            rightValue = other
        else:rightValue = self.exchange_rate[other.currency] * other.value

        return leftValue != rightValue

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rtruediv__ = __truediv__
    __rlt__ = __lt__
    __rle__ = __le__
    __rgt__ = __gt__
    __rge__ = __ge__
    __req__ = __eq__
    __rne__ = __ne__

x = Money(10, "USD")
y = Money(1000)
z = Money(12.34, "EUR")

print(z + 3.11 * x + y * 0.8)
lst = [Money(10,"EUR"), Money(1100), Money(12.01, "USD")]
s = sum(lst)
print(s)
