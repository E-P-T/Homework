def remember_result(func):
    prev = None
    def inner(*args):
        nonlocal prev
        print(f'Last result = {prev}') 
        prev = func(*args)
    return inner

@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result

sum_list("a", "b")
sum_list("abc", "cde")
sum_list('3', '4', '5')
