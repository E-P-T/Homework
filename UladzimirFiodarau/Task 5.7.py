### Task 4.7*
# Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
# Try to change x to a list `[1,2,3]`. Explain the result.
# Try to change import to `from x import *` where x - module names. Explain the result.

from mod_b import *
from mod_c import *

print(x)
# вывод будет 1000, т.к. произошло сначала импортирование модуля Б, который в свою очередь импортировал модуль С и в нем
# изменил значение Х на 1000
# В результате последующего импортирования из модуля С в модуль А импортируется уже измененное значение Х = 1000

x = [1,2,3]
print(x)
# вывод будет [1, 2, 3], т.к. в процессе работы программа присваивает локальной переменной Х  ссылку на новое значение


