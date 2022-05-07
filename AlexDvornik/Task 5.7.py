"""
Task 5.7*
Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
Try to change x to a list `[1,2,3]`. Explain the result.
Try to change import to `from x import *` where x - module names. Explain the result.
"""


"""
Basically, import order does not matter. If a module relies on other modules, it needs to import them itself.
However, if we use the "from x import * " paradigm, the code inside the x module will run first. Hence, the order of
imports will affect the final result
"""
