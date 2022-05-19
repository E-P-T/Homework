##### First Version #####
### mod_a ###
# from mod_b import *
# from mod_c import *
# print(x)

### mod_b ###
# import mod_c
# mod_c.x = 1000

### mod_c ###
# x = 6


##### Second Version #####
### mod_a ###
# from mod_b import *
# from mod_c import *
# print(x)

### mod_b ###
# import mod_c
# mod_c.x = 1000

### mod_c ###
# x = [1,2,3]


##### Third Version #####
### mod_a ###
# from mod_b import *
# from mod_c import *
# print(x)

### mod_b ###
# from mod_c import x
# x = 1000

### mod_c ###
# x = [1,2,3]


#===============================================================================================#


##### First Version #####
# In first version, in `mode_a` module, we are first importing all content of module `mod_b`.
#   in module mod_b, we are importing `mod_c` and modifying its variable `x`
# After the import of `mod_b`, we are importing everything from `mod_c`, which has been modified by `mod_b`
# Therefore, if we want to access the `x` variable of `mod_c`, we will not see its original value that was assigned from `mod_c`.
# Instead, we will see modified value from `mod_b`

##### Second Version #####
# In second version of code, we will see the same result as in version 1.
# The reason of it: we are changing x from `mod_c`, but `mod_b` modifies it no matter what value x holds initially

##### Third Version #####
# In third version of code, we can observe that variable `x` is exactly the variable that was imported from `mod_c`.
# Firstly, we have changed the way of assigning a new value to `x` in `mod_b`. 
# In previous cases, we modified the value of `x` of `mod_c` inside of `mod_b`. However, now, 
# in `mod_b`, our change concerns only `mod_b` module.
# And finally, the reason why we see the `x` from `mod_c` is just we are importing `mod_c` after the import of `mod_b`.