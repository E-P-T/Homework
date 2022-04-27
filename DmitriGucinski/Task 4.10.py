def generate_squares(num):
    return {num: num*num for num in range(1, num+1)}


print(
    generate_squares(5)
)
