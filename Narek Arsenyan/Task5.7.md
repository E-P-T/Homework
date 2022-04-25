
```
from mod_b import *
from mod_c import *

print(x)
```

# case 1 
In this case in mod_a.py firstly imports mod_b.py file, which overwrites mod_c.py variable **x**.
after that mod_c.py is imported in mod_a.py, but because x variable is already changed by mod_b.py, it outputs **1000**

# case 2
In this case when we change **x** value in mod_b.py, same is happening as in the case 1, so it outputs [1,2,3]

# case 3
Because there is no module with name **x**, it will throw error. 
