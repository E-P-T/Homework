from typing import List


def foo(num_list) -> List[int]:
    product = calculate_product(num_list)
    list = []
    for num in num_list:
        list.append(int(product / num))
    return list


def calculate_product(num_list) -> int:
    product = 1
    for num in num_list:
        product *= num
    return product


if __name__ == "__main__":
    print(foo([3, 2, 1]))
