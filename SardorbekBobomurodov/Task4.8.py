from typing import List, Tuple


def get_pairs(lst: List) -> List[Tuple]:
    return_list = []
    for index in range(len(lst)-1):
        return_list.append((lst[index], lst[index + 1]))
    return return_list


if __name__ == "__main__":
    print(get_pairs([1, 2, 3, 8, 9]))
