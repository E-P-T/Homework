from string import ascii_letters


def get_common_chars(*strings) -> set[str]:
    """ Function that takes a variable amount of strings, finds the common character for all strings.
        Returns it.
    """
    common_chars = set()

    chars_count = {
        char: 0
        for char in ascii_letters[:26]
    }

    for string in strings:
        string = set(string.lower())
        for char in string:
            chars_count[char] += 1
    
    for char, char_count in chars_count.items():
        if char_count == len(strings):
            common_chars.add(char)
    
    return common_chars


def get_used_chars(*strings) -> set[str]:
    """ Function that takes a variable amount of strings.
        Finds and returns the characters that appeared at least once in these strings.
    """
    used_chars = set()

    chars_count = {
        char: 0
        for char in ascii_letters[:26]
    }

    for string in strings:
        string = set(string.lower())
        for char in string:
            chars_count[char] += 1
    
    for char, char_count in chars_count.items():
        if char_count > 0:
            used_chars.add(char)

    return used_chars   


def get_active_chars(*strings) -> set[str]:
    """ Function that takes a variable number of strings.
        Finds and returns the characters that appeared in at least two strings.
    """
    active_chars = set()

    chars_count = {
        char: 0
        for char in ascii_letters[:26]
    }

    for string in strings:
        string = set(string.lower())
        for char in string:
            chars_count[char] += 1
    
    for char, char_count in chars_count.items():
        if char_count > 1:
            active_chars.add(char)

    return active_chars


def get_unused_chars(*strings) -> set[str]:
    """ Function that takes a variable amount of strings.
        Finds and returns the characters that have not appeared in any given string.
    """
    unused_chars = set()

    chars_count = {
        char: 0
        for char in ascii_letters[:26]
    }

    for string in strings:
        string = set(string.lower())
        for char in string:
            chars_count[char] += 1
    
    for char, char_count in chars_count.items():
        if char_count == 0:
            unused_chars.add(char)
            
    return unused_chars



if __name__ == "__main__":
    test_strings = ["Umid", "Saidumar", "Sardor", ]
    test_strings_2 = ["hello", "world", "python", ]
    print(get_common_chars(*test_strings))
    print(get_used_chars(*test_strings_2))
    print(get_active_chars(*test_strings_2))
    print(get_unused_chars(*test_strings_2))