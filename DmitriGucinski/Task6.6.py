from functools import total_ordering


@total_ordering
class Money:
    _value = None
    _currency = None
    _dollar_value = None
    
    exchange_rate = {
        "EUR": 0.93,
        "BYN": 2.1,
        "JPY": 2.5,
        "USD": 1.0,
    }
    
    def __init__(self, value, currency="USD"):
        self._value = value
        self._currency = currency
        self._dollar_value = self._convert_to_dollar_currency(self._value)
        
    def _convert_to_init_currency(self, value):
        return value * self.exchange_rate[self._currency]
        
    def _convert_to_dollar_currency(self, value):
        return value / self.exchange_rate[self._currency]        
                
    def __str__(self):
        return f"{self._value} {self._currency}"
        
    def __repr__(self):
        return f"Money({self._value}, '{self._currency}')"
    
    def __lt__(self, other):
        return self._dollar_value < other._dollar_value
    
    def __eq__(self, other):
        return self._dollar_value == other._dollar_value    
        
    def __add__(self, other):
        
        if isinstance(other, int) or isinstance(other, float):
            return Money(
                    self._convert_to_init_currency( 
                        self._dollar_value + other
                    ),
                    self._currency
                    )          
        if isinstance(other, Money):
            return Money(
                    self._convert_to_init_currency( 
                        self._dollar_value + other._dollar_value
                    ),
                    self._currency
                    )
                    
        raise ValueError()
    
    __radd__ = __add__        

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(
                    self._convert_to_init_currency( 
                        self._dollar_value * other
                    ),
                    self._currency
                    )          
        
        if isinstance(other, Money):
            return Money(
                    self._convert_to_init_currency( 
                        self._dollar_value * other._dollar_value
                    ),
                    self._currency
                    ) 
                    
        raise ValueError()                 
        
    __rmul__ = __mul__    
        
    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(
                    self._convert_to_init_currency( 
                        self._dollar_value - other
                    ),
                    self._currency
                    )          
        
        if isinstance(other, Money):
            return Money(
                    self._convert_to_init_currency( 
                        self._dollar_value - other._dollar_value
                    ),
                    self._currency
                    ) 
                    
        raise ValueError()                 
       
    __rsub__ = __sub__
              
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(
                    self._convert_to_init_currency( 
                        self._dollar_value / other
                    ),
                    self._currency
                    )          
        
        if isinstance(other, Money):
            return Money(
                    self._convert_to_init_currency( 
                        self._dollar_value / other._dollar_value
                    ),
                    self._currency
                    ) 
                    
        raise ValueError() 

        

f_money = Money(5, 'EUR')
s_money = Money(10)

print(f_money._dollar_value)
print(s_money._dollar_value)

print( str(f_money) )
print( repr(f_money) )

print(f_money == s_money)
print(f_money < s_money)
print(f_money > s_money)

print(f_money + s_money)
print(f_money - s_money)

lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)

print(s)

x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8) # result in “EUR”

print(dir(Money))
print(x._value)
print(Money(100,"BYN") / 10 )


