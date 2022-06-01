def call_once(func):
    cache = 0
    def wrapper(a, b):
        nonlocal cache
        if cache == 0:    #this works one times
            cache = func(a,b)       
        return cache
    return wrapper    
    
@call_once
def sum_of_numbers(a, b):
    return a + b
    
print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(134, 412))