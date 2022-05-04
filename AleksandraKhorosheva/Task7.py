### Task 4.7*
'''Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
Try to change x to a list `[1,2,3]`. Explain the result.
Try to change import to `from x import *` where x - module names. Explain the result.'''

'''
When we use 'import module', the order is not important, the variable X is subtracted at the time of conversion, 
the code of module B and C will be executed before that. When we use 'from module import *', the order is important, 
if we want to get X from module C, we need to write it first. Such an entry already writes the value to a local variable.
'''
