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

# разница между способами импорта "import mod_b" и "from mod_b import *" заключается в том что:
# при первом варианте
# в пространство имен программы загружается имя модуля и доступ к функциям модуля осуществляется в форме
# <имя_модуля>.<имя_функции>. Это позволяет в значительной мере избежать конфликтов имен импортируемых функций однако
# создает некоторые неудобства при их именовании для вызова (особенно у модулей с большими названиями, хотя и это можно
# обойти присвоением модулю нового имени конструкцией "import functools as f", к примеру)
# при втором варианте:
# в текущую программу будут импортированы все переменные из списка __all__ в импортируемом модуле (или все кроме тех,
# имена которых начинаются с подчеркивания (_), если список __all__ не обозначен). в таком формате импорта обращение к
# функциям осуществляется по их имени без указания имени модуля, что упрощает вызов но увеличивает шанс на конфликты
#  имен, особенно в объемных программах с большим количеством переменных.

