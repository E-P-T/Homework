def replace(my_string):
    return my_string.replace('"','~').replace("'",'"').replace('~',"'")
if __name__ == '__main__':
    my_string=input('Input your string: ')
    print(replace(my_string))