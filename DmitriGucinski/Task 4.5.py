def get_digits(num):
    return tuple(int(i) for i in str(num))


def get_dig(number):
    stack = []
    while number > 0:
        stack.insert(0, number % 10)
        number = number // 10

    return tuple(stack)


print(
    get_dig(87178291199)
)

print(
    get_digits(87178291199)
)
