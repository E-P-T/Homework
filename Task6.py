# Task 6.6

from functools import reduce, total_ordering


@total_ordering
class Money:
    """The class is able to exchange one currency for another."""

    currency_rate = {
        "USD": 1.0,
        "EUR": 0.93,
        "BYN": 2.10,
        "JPY": 127.94,
    }

    def __init__(self, amount, currency='USD'):
        """Initializer for class Money.

        Args:
            amount (float): amount of money to be exchanged.
            currency (str, optional): currency name. Defaults to 'USD'.
        """

        self._amount = amount
        self._currency = currency

    @staticmethod
    def currency_exchange(amount, currency, exc_currency):
        """Converts a certain amount of one currency into another.

        Args:
            amount (float): amount of money to be exchanged.
            currency (str): original currency.
            exc_currency (str): currency to which we change.

        Returns:
            float: amount of money exchanged.
        """

        a = amount
        b = Money.currency_rate[currency]
        c = Money.currency_rate[exc_currency]
        return a/b*c

    def __eq__(self, other):
        return self._amount == self.currency_exchange(
            other._amount, other._currency, self._currency)

    def __lt__(self, other):
        return self._amount < self.currency_exchange(
            other._amount, other._currency, self._currency)

    def __add__(self, other):
        v = self.currency_exchange(
            other._amount, other._currency, self._currency)
        return Money(self._amount+v, self._currency)

    def __sub__(self, other):
        v = self.currency_exchange(
            other._amount, other._currency, self._currency)
        return Money(self._amount-v, self._currency)

    def __mul__(self, other):
        v = self.currency_exchange(
            other._amount, other._currency, self._currency)
        return Money(self._amount*v, self._currency)

    def __truediv__(self, other):
        v = self.currency_exchange(
            other._amount, other._currency, self._currency)
        return Money(self._amount/v, self._currency)

    def __str__(self):
        return f'{round(self._amount, 2)} {self._currency}'

    def __radd__(self, other):
        return Money(self._amount+other, self._currency)


def main():
    """Main function."""

    print()
    print('{:*^30}'.format('The task 6.7'), end='\n\n')

    x = Money(10, "BYN")
    y = Money(12.34, "EUR")
    z = Money(11)

    print('{:=^30}'.format('+'*5))
    print(x + y + z)
    lst = [x, y, z]
    s = sum(lst)
    print(s)
    print('='*30, end='\n\n')

    print('{:=^30}'.format('-'*5))
    print(x - y - z)
    lst = [x, y, z]
    result = reduce((lambda x, y: x-y), lst)
    print(result)
    print('='*30, end='\n\n')

    print('{:=^30}'.format('*'*5))
    print(x * y * z)
    lst = [x, y, z]
    result = reduce((lambda x, y: x*y), lst)
    print(result)
    print('='*30, end='\n\n')

    print('{:=^30}'.format('/'*5))
    print(x / y / z)
    lst = [x, y, z]
    result = reduce((lambda x, y: x/y), lst)
    print(result)
    print('*'*30, end='\n\n')

    print('{:=^30}'.format(' <, <=, ==, !=, >=, > '))
    print(f'x < y: {x < y}')
    print(f'x <= y: {x <= y}')
    print(f'x == y: {x == y}')
    print(f'x != y: {x != y}')
    print(f'x >= y: {x >= y}')
    print(f'x > y: {x > y}')


if __name__ == '__main__':
    main()
