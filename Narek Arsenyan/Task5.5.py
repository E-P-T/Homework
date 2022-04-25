def remeberLastCall(func):
	a = None
	def innerFunc(*args):
		nonlocal a
		print(a)
		a = func(*args)
	return innerFunc

@remeberLastCall
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result
sum_list("asdfghjkl","gfdsa","hgfd")
sum_list("aa","bb","cc")
sum_list("1","kjj","jh")
