### Task 4.5
'''
Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.

```python
@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result

sum_list("a", "b")
"Last result = 'None'"
"Current result = 'ab'"
sum_list("abc", "cde")
"Last result = 'ab'"
"Current result = 'abccde'"
sum_list(3, 4, 5)
"Last result = 'abccde'"
"Current result = '12'"
```
'''


def remember_result(func):
    prev = None

    def wrapper(*args):
        nonlocal prev
        print(f"Last result = '{prev}'")
        res = func(*args)
        prev = res
        return res

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result

#sum_list = remember_result(sum_list)


sum_list("a", "b")
sum_list("abc", "cde")
sum_list("3","4","5")
