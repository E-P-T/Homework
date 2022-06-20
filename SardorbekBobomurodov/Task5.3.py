# File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
# This file contains the student’s names, age and average mark.
# 1) Implement a function which receives file path and returns names of top performer students
# ```python

#
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
# ```
#
# 2) Implement a function which receives the file path with srudents info and writes CSV student information to the new file in descending order of age.
# Result:
# ```
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27
# ```
path_name = r"C:\Users\Sardor\PycharmProjects\Homework\data\students.csv"


def get_top_performers(file_path, number_of_top_students):
    all_students = {}
    answer = []
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip('\n').split(',')
            all_students[row[0]] = row[2]
    del all_students['student name']
    all_students = sorted(all_students.items(), key=lambda x: x[1], reverse=True)

    for info in all_students:
        answer.append(info[0])
    return answer[:number_of_top_students]


def write_to_students(file_path, name, age, score):
    with open(file_path, 'w') as w_file:
        w_file.write("{},{},{}".format(name, age, score))


print(get_top_performers(path_name, 5))
