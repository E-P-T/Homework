def foo(list_int):
    output = []

    for i in range(len(list_int)):
        multiply = 1
        for k, num in enumerate(list_int):
            if k != i:
                multiply *= num
        output.append(multiply)

    return output


print(
    foo([1, 2, 3, 4, 5])
)


print(
    foo([3, 2, 1])
)
