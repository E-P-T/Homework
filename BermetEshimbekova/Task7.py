# Task 4.7

def foo(int_list):
    numbers = int_list.copy()
    products = []
    for i in numbers:
        product = 1
        int_list = list(numbers)
        int_list.pop(int_list.index(i))
        for ii in int_list:
            product *= ii
        products.append(product)
    print(products)


foo([1, 2, 3, 4, 5])
foo([3, 2, 1])
