
def generate_squares(num: int) -> dict:
    res = { i: i*i for i in range(1, num + 1) }
    return res

print(generate_squares(5))