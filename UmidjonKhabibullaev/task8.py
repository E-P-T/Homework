def get_pairs(lst: list) -> list[tuple]:
    """ Function to form the pairs of elements in `lst` list.
        Returns the list of tuples / pairs.
    """
    pairs = list()

    if len(lst) < 2:
        return None
    
    for i in range(1, len(lst)):
        pair = lst[i-1], lst[i]
        pairs.append(pair)
    
    return pairs


if __name__ == "__main__":
    elements = ['need', 'to', 'sleep', 'more']
    print(get_pairs(elements))