def isPalindrom(my_string):
    return my_string==my_string[::-1]
if __name__ == '__main__':
    my_string=input('Input your string: ')
    print(isPalindrom(my_string))