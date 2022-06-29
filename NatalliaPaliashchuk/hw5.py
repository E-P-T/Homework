# Homework-5_Working-with-data.md
# Совместный доступ
# P
# Свойства системы
# Тип
# Текст
# Размер
# 3 КБ
# Занимает
# 3 КБ
# Расположение
# Session 5
# Владелец
# Python Training
# Изменено
# 29 мар. 2022 г. (Python Training)
# Открыто
# 21:52 (я)
# Создано
# 28 апр. 2022 г.
# Описания нет
# Читателям разрешено скачивать файл
# # Python Practice - Session 4


# ### Task 4.1
# Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called `sorted_names.txt`. Each name should start with a new line as in the following example:

# ```
# Adele
# Adrienne
# ...
# Willodean
# Xavier
# ```
with open('data/unsorted_names.txt', 'r') as file, open('sorted_names.txt', 'w') as file_2:
    for name in sorted(file.readlines()):
        if '\n' in name:
            file_2.write(name)
        else:
            file_2.write(name + '\n')
            

# ### Task 4.2
# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.

# ```python
# def most_common_words(filepath, number_of_words=3):
#     pass

# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# ```

# > NOTE: Remember about dots, commas, capital letters etc.
def most_common_words(filepath, number_of_words=3):
    table = {39: 32, 34: 32, 46: 32, 44: 32, 63: 32, 33: 32, 58: 32, 59: 32, 92: 32, 47: 32}
    result = {}
    with open(filepath, 'r') as file:
        for line in file:
            for word in line.lower().translate(table).split():
                result[word] = result.get(word, 0) + 1
    return [word for word in sorted(result, key=lambda x: result[x], reverse=True)][:number_of_words]


# ### Task 4.3
# File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
# This file contains the student’s names, age and average mark. 
# 1) Implement a function which receives file path and returns names of top performer students
# ```python
# def get_top_performers(file_path, number_of_top_students=5):
#     pass

# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
def get_top_performers(file_path, number_of_top_students=5):
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            name, _, mark = line.split(sep=',')
            result.append((name, mark))
    return [name[0] for name in sorted(result[1:], key=lambda x: float(x[1]), reverse=True)][:number_of_top_students]
# ```

# 2) Implement a function which receives the file path with srudents info and writes CSV student information to the new file in descending order of age. 
# Result:
# ``` 
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27
# ```
def age_write_performers(file_path):
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            name, age, mark = line.split(sep=',')
            result.append((name, age, mark))
    with open(file_path[:-4] + '_new.csv', 'w') as file:
        file.write(','.join(result[0]))
        for line in [name for name in sorted(result[1:], key=lambda x: x[1], reverse=True)]:
            file.write(','.join(line))
            

# ### Task 4.4
# Look through file `modules/legb.py`.

# 1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():


        a = "I am local variable!"
        print(a)
        
    return inner_function   

# 2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        global a
        
        print(a)
        
    return inner_function   

# 2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.
a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():


        nonlocal a
        print(a)
        
        
    return inner_function   
 
 
# ### Task 4.5
# Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.

# ```python
# @remember_result
# def sum_list(*args):
# 	result = ""
# 	for item in args:
# 		result += item
# 	print(f"Current result = '{result}'")
# 	return result

# sum_list("a", "b")
# >>> "Last result = 'None'"
# >>> "Current result = 'ab'"
# sum_list("abc", "cde")
# >>> "Last result = 'ab'" 
# >>> "Current result = 'abccde'"
# sum_list(3, 4, 5)
# >>> "Last result = 'abccde'" 
# >>> "Current result = '12'"
# ```
def remember_result(func):
    result = None
    def wrapper(*args):
        nonlocal result
        print(f"Last result = '{result}'")
        result = func(*args)
    
    return wrapper

# ### Task 4.6
# Implement a decorator `call_once` which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.

# ```python
# @call_once
# def sum_of_numbers(a, b):
#     return a + b

# print(sum_of_numbers(13, 42))
# >>> 55
# print(sum_of_numbers(999, 100))
# >>> 55
# print(sum_of_numbers(134, 412))
# >>> 55
# print(sum_of_numbers(856, 232))
# >>> 55
# ```
def call_once(func):
    result = None
    def wrapper(*args, **kwargs):
        nonlocal result
        if result == None:
           result = func(*args, **kwargs)
        return result
    return wrapper
        


# ### Task 4.7*
# Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
# Try to change x to a list `[1,2,3]`. Explain the result.
# Try to change import to `from x import *` where x - module names. Explain the result. 


# ### Materials
# * [Decorators](https://realpython.com/primer-on-python-decorators/)
# * [Decorators in python](https://www.geeksforgeeks.org/decorators-in-python/)
# * [Python imports](https://pythonworld.ru/osnovy/rabota-s-modulyami-sozdanie-podklyuchenie-instrukciyami-import-i-from.html)
# * [Files in python](https://realpython.com/read-write-files-python/)