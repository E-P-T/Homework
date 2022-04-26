### Task 4.3
'''File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
This file contains the student’s names, age and average mark.
1) Implement a function which receives file path and returns names of top performer students
```python
def get_top_performers(file_path, number_of_top_students=5):
    pass
print(get_top_performers("students.csv"))
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']

2) Implement a function which receives the file path with students info and writes CSV student information to the new file in descending order of age.
Result:
```
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
'''
import csv


def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, "r", newline="") as csvfile:
        f = csv.reader(csvfile)
        next(f, None)
        all_students = [(r[0], int(r[1]), float(r[2])) for r in f]
        top_students = sorted(all_students, key=lambda x: x[2], reverse=True)[:number_of_top_students]
        return [x[0] for x in top_students]


print(get_top_performers("E:\PycharmProjects\Homework\data\students.csv"))


def get_sorted_file(file_path):
    with open(file_path, "r", newline="") as csvfile:
        read_file = csv.reader(csvfile)
        header = next(read_file, None)
        all_students = [(r[0], int(r[1]), float(r[2])) for r in read_file]
        sort_students = sorted(all_students, key=lambda x: x[1], reverse=True)
        with open("output/sort_students.csv", "w", newline="") as csvfile2:
            write_file = csv.writer(csvfile2)
            write_file.writerow(header)
            write_file.writerows(sort_students)


get_sorted_file("E:\PycharmProjects\Homework\data\students.csv")
