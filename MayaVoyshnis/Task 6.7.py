"""

### Task 4.7
Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:
```python
exchange_rate = {
    "EUR": 0.93,
    "BYN": 2.1,
    ...
}
```

Example:
```python
x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8) # result in “EUR”
>>543.21 EUR

lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s) #result in “BYN”
>>123.45 BYN
```

<em>Have a look at @functools.total_ordering</em>

"""


class Money:
    _exchange_rate = {
        'EUR': 0.93,
        'BYN': 2.1,
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
            return self.default_currency + other
        return self.default_currency + other.default_currency

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.default_currency - other
        return self.default_currency - other.default_currency

    __rsub__ = __sub__


if __name__ == '__main__':
    x = Money(10, "JPY")
    y = Money(11)
    print(x + y + x + 3)
    print(7 - x)
    # x = Money(10, "BYN")
    # y = Money(11)
    # z = Money(12.34, "EUR")
    # print(z + 3.11 * x + y * 0.8)
    #
    # lst = [Money(10, "BYN"), Money(11), Money(12.01, "USD")]
    # s = sum(lst)
    # print(s)
