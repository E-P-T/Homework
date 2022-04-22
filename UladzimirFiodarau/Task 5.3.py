# Task 5.3
# File `data/students.csv` stores information about students in [CSV]
# (https://en.wikipedia.org/wiki/Comma-separated_values) format.
# This file contains the student’s names, age and average mark.
# 1) Implement a function which receives file path and returns names of top performer students

# 2) Implement a function which receives the file path with students info and writes CSV student information
# to the new file in descending order of age.
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27

def get_top_performers(file_path: str, number_of_top_students: int = 5) -> list[str]:
    """
    The function receives file path and returns names of top performer students in form of a list (descending by
    average mark)
    :param file_path: path to input file
    :param number_of_top_students: number of top students to return
    :return: a list of strings
    :raises AssertionError if second argument is not integer
    """
    assert isinstance(number_of_top_students, int), 'Incorrect input, second argument must be an integer'
    with open(file_path, 'r', encoding='utf-8') as file:
        students_data = [[data for data in line.strip().split(',')] for line in file.readlines()[1:]]
        for data in students_data:
            data[1], data[2] = int(data[1]), float(data[2])
        return [data[0] for data in sorted(students_data, reverse=True, key=lambda x: x[2])[:number_of_top_students]]


print(get_top_performers("data/students.csv"))
# ['Josephina Medina', 'Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia']


def sort_students(file_path: str, sort_path: str = 'data/sorted_students.csv') -> None:
    """
    The function receives the file path with students info and writes CSV student information
    to a new file in descending order of age.
    :param file_path: path to input file
    :param sort_path: path to output sorted file
    :return: None
    """
    with open(file_path, 'r', encoding='utf-8') as inp_file, open(sort_path, 'w', encoding='utf-8') as out_file:
        print(inp_file.readline(), file=out_file, end='')
        students_data = [[data for data in line.strip().split(',')] for line in inp_file.readlines()]
        for data in students_data:
            data[1], data[2] = int(data[1]), float(data[2])
        print(students_data)
        for data in sorted(students_data, reverse=True, key=lambda x: x[1]):
            print(data, file=out_file)


sort_students("data/students.csv")
