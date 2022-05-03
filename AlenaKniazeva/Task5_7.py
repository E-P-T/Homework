"""
Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
Try to change x to a list `[1,2,3]`. Explain the result.
Try to change import to `from x import *` where x - module names. Explain the result.

"""

"""Solution

Task 1:
The thing is that import in python is performed only once. In mod_a.py we first import mod_b
file. File mod_b imports file mod_c and overwrites variable x. So we will have variable mod_c.x.
When we then import mod_c file, it will just create variable x, that will have the same value as
mod_c.x. It will not perform any other actions, because import mod_c was performed at stage of
import mod_b.

Task 2:
As was explained at task 1, as a result of comands from mod_a file
from mod_b import *
from mod_c import *
we will have two separate variavles mod_c.x and x. When we then change value x to [1,2,3],
command print(x) will just print the new value of x. Value of mod_c.x will stay the same.



Task 3: 
We will obtain an error, bacause thete is no module x.py

"""