
def get_digits(num: int) -> tuple[int]:
    res = []
    neg = False
    
    if num < 0:
        neg = True
        num = abs(num)

    num = num // 1

    while num > 0:
        res.append(num % 10)
        num = num // 10

    if neg:
        res.append('-')

    return tuple(reversed(res))

test = 87178291199
answer = (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
print(get_digits(test))
print(answer)
