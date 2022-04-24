# Task 5.3
# File data/students.csv stores information about students in CSV format. This file contains the student’s names,
# age and average mark.
#
# 1. Implement a function which receives file path and returns names of top performer students
#    def get_top_performers(file_path, number_of_top_students=5):
#        pass
#
#    print(get_top_performers("students.csv"))
#    >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']

# 2. Implement a function which receives the file path with students info and writes CSV student information
#    to the new file in descending order of age. Result:
#
#    student name,age,average mark
#    Verdell Crawford,30,8.86
#    Brenda Silva,30,7.53
#    ...
#    Lindsey Cummings,18,6.88
#    Raymond Soileau,18,7.27


def get_top_performers(file_path, number_of_top_students=5):

    """ a function which receives file path and returns names of top performer students """

    students_list = list()
    with open(file_path, 'r') as fd:
        for line in fd.readlines()[1:]:
            students_list.append(line.strip('\n').split(','))
    students_dict = dict()
    for student in students_list:
        students_dict[student[0]] = student[2]
    sorted_students_list = sorted(students_dict, reverse=True, key=lambda key: students_dict[key])
    top_performer_students = list()
    for key in sorted_students_list:
        if len(top_performer_students) == number_of_top_students:
            return top_performer_students
        top_performer_students.append(key)
    return top_performer_students


def descending_order_of_students_ages(file_path):

    """ a function which receives the file path with students info
        and writes CSV student information to the new file in descending order of age """

    students_list = list()
    with open(file_path, 'r') as fd:
        head = fd.readline().replace('\n', '').split(',')
        for line in fd.readlines():
            students_list.append(line.replace('\n', '').split(','))
    sorted_stds_list = sorted(students_list, reverse=True, key=lambda item : item[1])
    with open('std_age_descending.csv', 'w') as new_fd:
        new_fd.write(str(head[0]) + ', ' + str(head[1]) + ', ' + str(head[2]) + '\n')
        for item in sorted_stds_list:
            new_fd.write(str(item[0]) + ', ' + str(item[1]) + ', ' + str(item[2]) + '\n')
