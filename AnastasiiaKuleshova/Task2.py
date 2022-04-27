# Write a function that check whether a string is a palindrome or not. Usage of any reversing functions is prohibited.
# To check your implementation you can use strings from here.

def check_if_palindrom(line):
    line_without_spaces = line.replace(" ", "")
    chek_line = ""
    for i in range(len(line_without_spaces) - 1, -1, -1):
        chek_line += line_without_spaces[i]
    if (chek_line == line_without_spaces):
        print("This is palindrom")
    else:
        print("This is not palindrom")


check_if_palindrom("dogma i am god")
