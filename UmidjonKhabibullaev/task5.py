def remember_result(func):
	last_result = None # stores the results 
	def wrapper(*args):
		nonlocal last_result
		print(f"Last result = '{last_result}'")
		last_result = func(*args)
		
	return wrapper


@remember_result
def sum_list(*args):
	result = 0 if isinstance(args[0], int) else ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result


sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)

# sum_list("a", "b")
# >>> Last result = 'None'
# >>> Current result = 'ab'
# sum_list("abc", "cde")
# >>> Last result = 'ab'
# >>> Current result = 'abccde'
# sum_list(3, 4, 5)
# >>> Last result = 'abccde'
# >>> Current result = '12'