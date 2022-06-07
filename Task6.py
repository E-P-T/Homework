# Task 6.6
class Money:

    currency_rate = {
        "USD": 1.0,
        "EUR": 0.93,
        "BYN": 2.10,
        "JPY": 127.94,
    }

    def __init__(self, amount, currency='USD'):
        self._amount = amount
        self._currency = currency
