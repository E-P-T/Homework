# Task 6.6
class Money:

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
