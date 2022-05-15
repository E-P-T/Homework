def all_string_appear(lst):
    lst = [set(el) for el in lst]
    for i in range(1, len(lst)):
        res = lst[i - 1].intersection(lst[i])
    return res


def once_appear(lst):
    return set(''.join(lst))


def not_used(lst):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    return set(filter(lambda letter: not (letter in once_appear(lst)), alpha))


if __name__ == '__main__':
    lst = ["hello", "world", "python"]
    print(all_string_appear(lst))
    print(once_appear(lst))
    print(not_used(lst))
