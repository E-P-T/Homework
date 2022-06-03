import string


def test_1_1(text) -> list:
    return list(set.intersection(*map(set, text)) if text else set())


def test_1_2(text) -> list:
    return list(set.union(*map(set, text)) if text else set())


def test_1_3(*text):
    res = set()

    for i in text:
        for j in text:
            if i != j:
                res |= set(i) & set(j)
    return list(res)


def test_1_4(text):
    return set(string.ascii_lowercase) - set(test_1_2(text))


if __name__ == "__main__":
    test_strings = ["hello", "world", "python"]
    print(test_1_1(test_strings))
    print(test_1_2(test_strings))
    print(test_1_3(*test_strings))
    print(test_1_4(test_strings))
