# Task 5.3
# File data/students.csv stores information about students in CSV format. This file contains the student’s
# names, age and average mark. 1) Implement a function which receives file path and returns names of top
# performer students ```python def get_top_performers(file_path, number_of_top_students=5): pass
# print(get_top_performers(“students.csv”))
# [‘Teresa Jones’, ‘Richard Snider’, ‘Jessica Dubose’, ‘Heather Garcia’, ‘Joseph Head’] ```
# 2) Implement a function which receives the file path with srudents info and writes CSV student information to
# the new file in descending order of age. Result: student name,age,average mark Verdell Crawford
# 30,8.86 Brenda Silva,30,7.53 ... Lindsey Cummings,18,6.88 Raymond Soileau,18,7.27

import csv
import os


def get_top_performers(file_path, number_of_top_students=5):
    """
    Search `number_of_top_students` top performer students in `file_path`.
    """
    result = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)

        lst = sorted(reader, key=lambda t: float(t['average mark']), reverse=True)
        lst = lst[0:number_of_top_students]

        return [student['student name'] for student in lst]


def sort_students(src_path):
    """
    Generate from `file_path` a new csv-file, sorted by age in decsending order.
    """
    dst_path = os.path.join("..", "data", "sorted_students.csv")

    with open(src_path, 'r') as src, open(dst_path, 'w') as dst:
        reader = csv.DictReader(src)
        lst = sorted(reader, key=lambda t: t['age'], reverse=True)

        writer = csv.DictWriter(dst, reader.fieldnames)
        writer.writeheader()
        writer.writerows(lst)


def main():
    """
    Entry point function.
    """
    file_path = os.path.join("..", "data", "students.csv")
    print(get_top_performers(file_path, 3))
    print(get_top_performers(file_path))

    sort_students(file_path)


if __name__ == '__main__':
    main()
