# Task 4.10
'''Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number.
```python
print(generate_squares(5))н
 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''


def square_of_number(n):
    return {i: i*i for i in range(1, n+1)}
    # dic = {}
    # for i in range(1, n + 1):
    #     dic[i]=i*i
    # return dic


print(square_of_number(5))

