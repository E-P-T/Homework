def custom_split(string, delimeter = " "):
    """ Function to split a given `string` by a given `delimeter`.
        Returns the list of splitted substrings.
    """
    substrings = list()

    substring = ""
    for char in string:
        if char == delimeter:
            substrings.append(substring)
            substring = ""
            continue
        substring += char
    substrings.append(substring)

    return substrings


if __name__ == "__main__":
    s = "Umid,Aziza,Kamila"
    print(custom_split(s, ","))