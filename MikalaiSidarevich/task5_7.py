# Task 5.7*
"""
# mod_a
from mod_b import *
from mod_c import *
print(x)

# mod_b
import mod_c
mod_c.x = 1000

# mod_c
x = 6
"""

# Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
"""
from mod_b import * изменяет переменную x из модуля mod_c значением 1000.
from mod_c import * имортирует имя переменной x из модуля mod_c в данный.
print(x) выводит значение переменной x из модуля mod_c - оно равно 1000.
"""

# Try to change x to a list `[1,2,3]`. Explain the result.
"""
Если в mod_c изменить x = [1,2,3], то будет такой же результат, т.к. модуль mod_b изменит x на 1000.
"""
