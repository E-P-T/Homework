### Task 5.4
Look through file `modules/legb.py`.

1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.

2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.

2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.

### Task 5.5
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
>>> "Last result = 'None'"
>>> "Current result = 'ab'"
sum_list("abc", "cde")
>>> "Last result = 'ab'" 
>>> "Current result = 'abccde'"
sum_list(3, 4, 5)
>>> "Last result = 'abccde'" 
>>> "Current result = '12'"
```

### Task 5.6
Implement a decorator `call_once` which runs a function or method once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.

```python
@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
>>> 55
print(sum_of_numbers(999, 100))
>>> 55
print(sum_of_numbers(134, 412))
>>> 55
print(sum_of_numbers(856, 232))
>>> 55
```


### Task 5.7*
Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
Try to change x to a list `[1,2,3]`. Explain the result.
Try to change import to `from x import *` where x - module names. Explain the result. 


### Materials
* [Decorators](https://realpython.com/primer-on-python-decorators/)
* [Decorators in python](https://www.geeksforgeeks.org/decorators-in-python/)
* [Python imports](https://pythonworld.ru/osnovy/rabota-s-modulyami-sozdanie-podklyuchenie-instrukciyami-import-i-from.html)
* [Files in python](https://realpython.com/read-write-files-python/)
