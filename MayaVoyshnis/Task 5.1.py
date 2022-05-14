def sort_names(file_name):
    with open(file_name, "r") as unsorted_file:
        text = unsorted_file.read().split('\n')
    text.sort()
    with open('../data/sorted_names.txt', "w") as sorted_file:
        [sorted_file.write(name + '\n') for name in text]


if __name__ == '__main__':
    # file_name=input('Input path to the file')
    file_name = '../data/unsorted_names.txt'
    sort_names(file_name)