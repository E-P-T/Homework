import csv

def get_third_elem(iterable):
    return iterable[2]

def get_second_elem(iterable):
    return iterable[1]

def get_first_item(iterable):
    return iterable[0]

def get_top_performers(file_path = '../data/students.csv', number_of_top_students=5):
    data = csv.reader(open(file_path), delimiter=',')
    g = sorted(data, key= get_third_elem)
    a = g[-number_of_top_students-1:-1]
    a.reverse()
    s = list(map(get_first_item, a))
    return s
print(get_top_performers())


def writeSortedStudents(file_path = '../data/students.csv'):
    data = csv.reader(open(file_path), delimiter=',')
    g = sorted(data, key=get_second_elem)
    g.reverse()
    # print(g)
    with open('sortedStudents.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(g)
writeSortedStudents()
