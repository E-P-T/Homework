#! /usr/bin/env python
# File `data/students.csv` stores information about students in [CSV] format.
# This file contains the student’s names, age and average mark.
# 1) Implement a function which receives file path and returns
# names of top performer students
# >>> python
# def get_top_performers(file_path, number_of_top_students=5):
#     pass
# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider',
# 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
# 2) Implement a function which receives the file path with students info and
# writes CSV student information to the new file in descending order of age.
# Result:
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27


"""
task_3.py: implemented 4 functions according to the task and speed tests for
this functions. Module also contains conclusion about performance.
"""


import timeit
import pandas
import csv
from numpy import average as avg


def get_top_performers(filepath, number_of_top_students=5):
    """
    get_top_performers: reads students from csv file with path <filepath>.
    Returns top students using pandas module.
    Number of students takes from argument number_of_top_students.
    """
    data = pandas.read_csv(filepath)
    data = data.sort_values(by=["average mark"], ascending=False)
    return [data.iloc[i][0] for i in range(number_of_top_students)]


def write_students_to_file(filepath):
    """
    write_students_to_file: writes students in another file with path
    <filepath> which is sorted in descending order by age using pandas module.
    """
    data = pandas.read_csv(filepath)
    data = data.sort_values(by=["age"], ascending=False)
    data.to_csv(filepath[:-4] + "_new.txt", index=False)


def get_top_performers2(filepath, number_of_top_students=5):
    """
    get_top_performers2: reads students from csv file with path <filepath>.
    Returns top students using csv module.
    Number of students takes from argument number_of_top_students.
    """
    csv_file = open(filepath, 'r', newline='')
    reader = csv.reader(csv_file)
    next(reader)

    students = {row[0]: float(row[2]) for row in reader}
    students = sorted(
        students.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return [students[i][0] for i in range(number_of_top_students)]


def write_students_to_file2(filepath):
    """
    write_students_to_file: writes students in another file with path
    <filepath> which is sorted in descending order by age using csv module.
    """
    csv_file = open(filepath, 'r', newline='')
    reader = csv.reader(csv_file)

    header = next(reader)
    rows = [[row[0], float(row[1]), float(row[2])] for row in reader]
    rows.sort(key=lambda row: row[1], reverse=True)

    csv_file = open(filepath[:-4] + "_new.txt", 'w', newline='')
    writer = csv.writer(csv_file)

    writer.writerow(header)
    writer.writerows(rows)


if __name__ == "__main__":
    print(get_top_performers("data/students.csv"))
    # Result: ['Josephina Medina', 'Richard Snider', 'Teresa Jones',
    # 'Heather Garcia', 'Jessica Dubose']
    write_students_to_file("data/students.csv")

    print(get_top_performers2("data/students.csv"))
    # Result: ['Josephina Medina', 'Richard Snider', 'Teresa Jones',
    # 'Heather Garcia', 'Jessica Dubose']
    write_students_to_file2("data/students.csv")

    result = timeit.repeat(
        stmt="""get_top_performers("data/students.csv")""",
        number=100,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.1803518916003668

    result = timeit.repeat(
        stmt="""write_students_to_file("data/students.csv")""",
        number=100,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.34029944799985967

    result = timeit.repeat(
        stmt="""get_top_performers2("data/students.csv")""",
        number=100,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.06418457759937155

    result = timeit.repeat(
        stmt="""write_students_to_file2("data/students.csv")""",
        number=100,
        repeat=5,
        globals=globals()
    )
    print(avg(result))  # Result: 0.16175238120122232

    # As we can see csv module is better in case of performance, but as to
    # readability pandas is better.
