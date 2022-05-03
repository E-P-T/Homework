# Task 5.3
# File data/students.csv stores information about students in CSV format.
# This file contains the student’s names, age and average mark.
#
# Implement a function which receives file path and returns names of top performer students
# def get_top_performers(file_path, number_of_top_students=5):
#     pass
#
# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
# Implement a function which receives the file path with srudents info and writes CSV
# student information to the new file in descending order of age. Result:
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27

import csv
from operator import itemgetter


def csv_to_sorted_list_by_path_and_key(file_path, key):
    list_of_performers = []
    with open(file_path, 'r') as students:
        student_reader = csv.reader(students)
        is_header = True
        for row in student_reader:
            if is_header is True:
                is_header = False
                continue
            row[2] = float(row[2])
            list_of_performers.append(row)
    return sorted(list_of_performers, key=itemgetter(key), reverse=True)


def get_top_performers(file_path, number_of_top_students=5):
    sorted_list = csv_to_sorted_list_by_path_and_key(file_path, 2)
    return sorted_list[0:number_of_top_students]


# print(get_top_performers('..\\data\\students.csv'))


def students_by_age(file_path):
    students_sorted_by_age_path = '.\\data\\Task3_students_in_desc_order'
    sorted_list = csv_to_sorted_list_by_path_and_key(file_path, 1)
    with open(students_sorted_by_age_path, 'w', newline='') as students_file:
        writer = csv.writer(students_file)
        writer.writerows(sorted_list)


students_by_age('..\\data\\students.csv')
