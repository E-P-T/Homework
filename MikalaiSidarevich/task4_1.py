# Task 4.1
# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa.

def replace_quotes(s: str, reverse=False) -> str:
    """
    Replace quotes in `s`: " -> ' if `reverse`=False, ' -> " if `reverse`=True.
    """
    old, new = ("'", '"') if reverse else ('"', "'")
    return s.replace(old, new)


def main():
    """
    Entry point function.
    """
    s = "Single 'quotes' and double \"quotes\""
    print(f"input: {s}")
    print(f"\" > ': {replace_quotes(s)}")
    print(f"' > \": {replace_quotes(s, True)}")


if __name__ == '__main__':
    main()
