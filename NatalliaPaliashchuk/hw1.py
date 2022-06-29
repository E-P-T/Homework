# Homework-2_Python-Data_Types.md
# Совместный доступ
# P
# Свойства системы
# Тип
# Текст
# Размер
# 2 КБ
# Занимает
# 2 КБ
# Расположение
# Session 2
# Владелец
# Python Training
# Изменено
# 6 апр. 2022 г. (Python Training)
# Открыто
# 12:15 (я)
# Создано
# 6 апр. 2022 г.
# Описания нет
# Читателям разрешено скачивать файл
# # Python Practice - Session 2

# ### Task 2.1
# Write a Python program to calculate the length of a string without using the `len` function.
count = 0
for i in 'stroka\\n':
    count += 1

# ### Task 2.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
# Examples:
# ```
# Input: 'Oh, it is python' 
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
strng = 'Oh, it is python'
result = {}
for smbl in strng:
    result[smbl] = strng.count(smbl)
print(result)

# ```

# ### Task 2.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
# Examples:
# ```
# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white', 'red']
# ```
lst = ['red', 'white', 'black', 'red', 'green', 'black']
print(sorted(list(set(lst))))

# ### Task 2.3
# Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
# Examples:
# ```
# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
# ```
dig = 60
result = []
for nmbr in range(1, dig+1):
    if dig%nmbr == 0:
        result.append(nmbr)
print(result)   

# ### Task 2.4
# Write a Python program to sort a dictionary by key.
dic = {2: 1, 3: 1, 1: 2} 
dict(sorted(dic.items()))

# ### Task 2.5
# Write a Python program to print all unique values of all dictionaries in a list.
# Examples:
# ```
# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# ```
list_ = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
result = set()
for _ in list_:
    result.add(list(_.values())[0])
    
print(result)

# ### Task 2.6
# Write a Python program to convert a given tuple of positive integers into an integer. 
# Examples:
# ```
# Input: (1, 2, 3, 4)
# Output: 1234
# ```
tpl = (1, 2, 3, 4)
result = ''
for _ in tpl:
   result += str(_)
   
int(result)


# ### Task 2.7
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
# ```
# Input:
# a = 2
# b = 4
# c = 3
# d = 7

# Output:
# 	3	4	5	6	7	
# 2	6	8	10	12	14	
# 3	9	12	15	18	21	
# 4	12	16	20	24	28
# ```
a = 2
b = 4
c = 3
d = 7
for i in range(a - 1, b + 1):
    for j in range(c - 1, d +1):
        if i == a - 1 and j == c - 1:
            print(' ', end='\t')
        elif i == a - 1:
            print(j, end='\t')
        elif j == c - 1:
            print(i, end='\t')
        else:
            print(i * j, end='\t')
    print()

# ### Materials
# * [Python Data Types](https://realpython.com/python-data-types/)
# * [Python Data Structures](https://realpython.com/python-data-structures/)
# * [Conditional Statements](https://realpython.com/python-conditional-statements/)
# * [While loop](https://realpython.com/python-while-loop/)
# * [For loop](https://realpython.com/python-for-loop/)
# * [Operators](http://pythonicway.com/python-operators)
