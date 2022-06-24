
def get_shortest_word(s: str) -> str:
    words = s.split()
    res = ""
    max_length = 0

    for word in words:
        if len(word) > max_length:
            res = word
            max_length = len(word)

    return res

# Variable number of tuples, which have design such as : ( (args[], kwargs{}), output )
def test_func(f, *args : tuple) -> None:
    
    for test in args:
        inpt, outpt = test
        args_, kwargs_ = inpt

        if args_ is None:
            args_ = []
        if kwargs_ is None:
            kwargs_ = {}

        result = f(*args_, **kwargs_)

        print(f.__name__, inpt, " -> ", result)
        print("Expected", outpt)
        print("Correct - {}".format("Yes" if result == outpt else "No"))
        print("-" * 40)


# List[tuples( in, out )]
test_case1 = ( (['Python is simple and effective!'], None), 'effective!' )
test_case2 = ( (['Any pythonista like namespaces a lot.'], None), 'pythonista' )

test_cases = [test_case1, test_case2]

test_func(get_shortest_word, *test_cases)
