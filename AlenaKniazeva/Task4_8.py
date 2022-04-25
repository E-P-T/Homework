"""This program contains a a function `get_pairs(lst: List) -> List[Tuple]`
which returns a list of tuples containing pairs of elements"""

def get_pairs(*inp_list):
    if len(inp_list) > 1:
        return [tuple(inp_list[i:i+2]) for i in range(len(inp_list)-1)]
    else:
        return None

if __name__ == "__main__":
    inp = [s.strip("'") for s in input("Enter a list: ").strip('[]').split(', ')]
    print("Resulting list of tuples: {}".format(get_pairs(*inp)))