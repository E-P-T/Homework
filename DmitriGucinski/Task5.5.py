#Implement a decorator remember_result which remembers last result of function it decorates and prints it before next call.

def remember_result(func):
    result = None
    def wrapper(*args):
        nonlocal result
        print(f"Last result = {result}")
        result = func(*args)
        return result
    return wrapper    

@remember_result
def sum_list(*args):
    result = 0 if isinstance(args[0], int) else ""          
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result
    
    
sum_list('aa', 'b')

sum_list('ab', 'c')

sum_list('a', 'b')

sum_list(1,2)
