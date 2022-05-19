# def remember_result(func):
#     result = None
#     def wrapper(*args):
#         nonlocal result
#         print(f"Last result = {result}")
#         result = func(*args)
#         return result
#     return wrapper    

# @remember_result
# def sum_list(*args):
#     result = 0 if isinstance(args[0], int) else ""          
#     for item in args:
#         result += item
#     print(f"Current result = '{result}'")
#     return result



def test_deco(func):
    counter = 0
    def wrapper():
        nonlocal counter
        print(counter)
        counter += 1
    print("Test deco's call")        
    wrapper()
    wrapper()
    return wrapper
@test_deco
def say_hi():
    print("Hi Forceward!")

test_deco(say_hi)
# say_hi()
# say_hi()

# say_hi = test_deco(say_hi) | wrapper