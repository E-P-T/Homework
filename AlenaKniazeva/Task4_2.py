"""This program checks whether a string is a palindrome or not"""

def palindrome(s):
    ans = '' if s == s[::-1] else 'not '     # checking and answering
    print("The string is {}a palindrome".format(ans))

if __name__ == "__main__":
    in_s = input("Enter a string: ")
    palindrome(in_s)