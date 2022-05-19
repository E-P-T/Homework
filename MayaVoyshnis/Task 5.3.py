def get_top_performers(file_path, number_of_top_students=5):
    lst = make_lst_from_file(file_path)
    lst.sort(key=lambda x: float(x[2]))
    return list(map(lambda x: x[0], lst[-1:-1 * (number_of_top_students + 1):-1]))


def creat_file_sorted_of_age(file_path):
    lst = make_lst_from_file(file_path)
    lst.sort(key=lambda x: int(x[1]))
    file = open('new.csv', 'w')
    file.write('student name,age,average mark\n')
    for student in reversed(lst):
        file.write(' '.join(student) + '\n')


def make_lst_from_file(file_path):
    return list(map(lambda line: line.replace('\n', '').split(','), open(file_path)))[1::]


if __name__ == '__main__':
    get_top_performers("/repositories/HomeTask/data/students.csv")
    creat_file_sorted_of_age("/repositories/HomeTask/data/students.csv")
