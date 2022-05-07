'''
Task 5.3
File `data/students.csv` stores information about students in [CSV] format.
This file contains the student’s names, age and average mark.
1) Implement a function which receives file path and returns names of top performer students

def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']

2) Implement a function which receives the file path with srudents info and writes CSV student information to the new
file in descending order of age.
Result:
student name,age,average mark

Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
'''
import csv
from decorators import converter


# Task 5.3.1
@converter
def csv_to_list(file_path):
    data = []
    with open(file_path, 'r') as inf:
        reader = csv.reader(inf)
        header = next(reader)
        for line in reader:
            dict_of_students = {}
            n = 0
            for item in header:
                dict_of_students[item] = line[n]
                n += 1
            data.append(dict_of_students)
        return data


def get_top_performers(file_path, number_of_top_students=5):
    lst = sorted(csv_to_list(file_path), key=lambda x: x['average mark'], reverse=True)
    list_of_names = []
    for element in lst:
        for key, value in element.items():
            if key == 'student name':
                list_of_names.append(element[key])
    return list_of_names[:number_of_top_students]


# Task 5.3.2
def sort_by_age(file_path):
    lst = sorted(csv_to_list(file_path), key=lambda x: x['age'], reverse=True)
    headers = lst[0].keys()
    with open('data/students_out.txt', 'w') as outf:
        writer = csv.DictWriter(outf, headers)
        writer.writeheader()
        writer.writerows(lst)


if __name__ == '__main__':
    fpath = 'data/students.csv'
    print(get_top_performers(fpath))
    sort_by_age(fpath)
