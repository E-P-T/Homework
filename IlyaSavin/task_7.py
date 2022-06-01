#! /usr/bin/env python
# TODO: Run the module `modules/mod_a.py`. Check its result.
# Explain why does this happen.
# Try to change x to a list `[1,2,3]`. Explain the result.
# Try to change import to `from x import *` where x - module names.
# Explain the result.


# 1. When we run modules/mod_a.py first of all "from mod_b import *" is executed.
# When it's executed then in modules/mod_b.py "import mod_c" is executed.
# When it's executed then in modules/mod_c.py "x = 6" is executed
# and then in modules/mod_b.py module_object "mod_c" was created.
# That's mean that mod_c appended to sys.modules and it's located in RAM now.
# Then in modules/mod_b.py "mod_c.x = 1000" is executed.
# After that mod_b appended to sys.modules and it's located in RAM now.
# After all in modules/mod_a "from mod_c import *" is executed, but mod_c was
# in RAM and it simply takes module_object mod_c from sys.modules.
# Result is 1000 because in mod_b.py x was changed but in mod_a.py statement
# "from mod_c import *" doesn't perform code of mod_c.py because it was in
# RAM by that time.


# 2. When we change x to [1, 2, 3] in mod_a, x will be [1, 2, 3] but only in
# mod_a. If any other module will import mod_b it will be 1000, if any other
# module will import mod_c it will be 6. It's just because statement
# "from module import smth" is just copying. It's work like assigment.
# Example: from mod_z import x is equal to import mod_z; x = mod_z.x; del mod_z
# When x will be changed it force variable x refs to other object in memory.
# But mod_z.x stays the same as it was.


# 3. It was in the task, so I explained it before. If I need to explain
# difference between import module and from module import vars it's ok.
# The difference is that the first statement creates module_object and
# use it like container. The second only copies vars from module. It doesn't
# save module object. That's all. There are some consequences like I said before.
