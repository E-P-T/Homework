def to_dict(number):
    final_dict = {i: i*i for i in range(1, number + 1)}
    return final_dict

num = int(input("num = "))
print(to_dict(num))