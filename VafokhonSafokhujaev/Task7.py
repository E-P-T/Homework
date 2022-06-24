def foo(array: list[int]) -> list[int]:
    dividend = 1
    for el in array:
        dividend *= el

    return [dividend // el for el in array]

# List[tuples( in, out )]
test_cases = []
test_cases.append( ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24] ) )
test_cases.append( ([3, 2, 1], [2, 3, 6] ) )

for test in test_cases:
    inp, out = test
    res = foo(inp)
    print(foo.__name__, inp, " -> ", res)
    print("Expected", out)
    print("Correct - {}".format("Yes" if res == out else "No"))
    print("-" * 40)