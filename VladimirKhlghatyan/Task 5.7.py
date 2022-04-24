# Task 5.7*
# Run the module modules/mod_a.py. Check its result. Explain why does this happen.
# Try to change x to a list [1,2,3]. Explain the result.
# Try to change import to from x import * where x - module names. Explain the result.

from mod_b import *
from mod_c import *

print(x)

# ___1___
# В модуле mod_b импортируется модуль mod_c и в нем изменяется значение "x" на 1000 (x = 1000). Поэтому при импорте
# в mod_a модуля mod_b сначала меняется знащение "x" в модуле mod_c, а потому модуль mod_c импортируется в mod_a.
# Вывод программы будет 1000.

# ___2___
# При изменении mod_b (x = [1, 2, 3]) принцип работы кода в mod_a не меняется,
# т.к. в mod_b локальной переменной "x" всего лишь присваивает ссылку на новое значение ([1, 2, 3]).
# Вывод программы будет [1, 2, 3].

# ___3___
# При попыытке импортирошать модулч "x" программа выдаст ошибку,
# т.к. ш текущей директории не существует модлч по имении "x".
