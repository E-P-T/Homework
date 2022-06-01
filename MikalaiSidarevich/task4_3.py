# Task 4.3
# Implement a function which works the same as `str.split` method
# (without using `str.split` itself, ofcourse).

def custom_split(s: str, sep: str = None, maxsplit: int = -1) -> list[str]:
    """
    Custom `str.split` method implementation.
    """
    result = []
    word, rest = '', s

    # Splits counter
    counter, enabled = 0, True

    # Disable counter if maxsplit is invalid
    if maxsplit < 0:
        enabled = False

    if not sep:
        sep = ' '

    i = 0
    while i < len(s) and ((counter < maxsplit) ^ (not enabled)):
        if s[i:i+len(sep)] == sep:
            result.append(word)
            word = ''
            rest = s[i+len(sep):]
            i += len(sep)

            # Don't count splits if maxsplit invalid
            if enabled:
                counter += 1
        else:
            word += s[i]
            i += 1
    else:
        # Consider the last element
        result.append(rest)
    return result


def main():
    """
    Entry point function.
    """
    s = "Implement a function which works the same as `str.split` method."
    print(f"Python: {s.split()}")
    print(f"Custom: {custom_split(s)}")
    print(f"Python: {s.split(' a')}")
    print(f"Custom: {custom_split(s, ' a')}")
    print(f"Python: {s.split(maxsplit=5)}")
    print(f"Custom: {custom_split(s, maxsplit=5)}")


if __name__ == '__main__':
    main()
