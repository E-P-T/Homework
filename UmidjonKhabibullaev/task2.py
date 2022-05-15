def is_polidrome(string: str) -> bool:
    """ Function that checks whether a given string is polindrome or not.
        Returns the boolean value representing that.
    """

    for i in range(len(string) - 1):
        if string[i] != string[-1 - i]:
            return False

    return True


if __name__ == "__main__":
    s1 = "aziza"
    s2 = "hurray"
    s3 = "polindrome"
    s4 = "mom"

    s_list = [s1, s2, s3, s4]

    for string in s_list:
        print(f"{string}: {is_polidrome(string)}")
