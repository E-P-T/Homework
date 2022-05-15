def get_digits(num):
    my_tuple=[char for char in str(num) if char.isdigit()]
    print(tuple(my_tuple))

if __name__ == '__main__':
    get_digits('8f7178291199')
