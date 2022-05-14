
def call_once(func):
    '''runs a function or method once and caches the result. All consecutive calls to this function should return cached result no matter the arguments.'''
    
    
@call_once
def sum_of_numbers(a, b):
    return a + b
    
print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(134, 412))
