def ex5(some_dict):
    print(some_dict)
    sorted_keys = sorted(some_dict.keys())
    new_dict = {}
    for key in sorted_keys:
        new_dict[key] = some_dict[key]
    print(new_dict)


if __name__ == "__main__":
    someDict = {3: 'Geeks', 1: 'Geeks', 2: 'For', 4: 'Python', 5: 'EPAM'}
    ex5(someDict)
