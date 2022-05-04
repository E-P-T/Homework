# ### Task 5.7*

# Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.

# Try to change x to a list `[1,2,3]`. Explain the result.

# Try to change import to `from x import *` where x - module names. Explain the result.

## case 1

In this case in `mod_a` firstly imports `mod_b` , which overwrites mod_c.py variable x.
 after that `mod_c` is imported in `mod_a` , but because x variable is already changed by `mod_b` , it outputs `1000`

## case 2

When we change `x` value in `mod_b` , we get the same result as in 1st case, so the output is `[1,2,3]`

## case 3

Since there is no module with name `x` , we'll get an error.
