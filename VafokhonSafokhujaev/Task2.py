def is_palindrome(string):

    # This part makes function aplicable for checking of only characters
    # Example : A man, a plan, a canal – Panama
    string = "".join([c for c in string if c.isalpha()])
    string = string.lower()

    str_length = len(string)
    palindrome = True

    for i in range(str_length):
        if string[i] != string[str_length-i-1]:
            print(string[i], string[str_length-i-1])
            palindrome = False
            break

    return palindrome


text = input()
print(is_palindrome(text))