"""Task 4.3
File data/students.csv stores information about students in CSV format. This file contains the student’s names,
age and average mark.

    1.Implement a function which receives file path and returns names of top performer students
    def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))
> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']

    2.Implement a function which receives the file path with srudents info and writes CSV student
    information to the new file in descending order of age. Result:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""

import csv
def get_top_performers(file_path, number_of_top_students=5):

    with open(file_path, newline = "") as f:
        lst = csv.reader(f, delimiter=",")
        sorted_data = sorted(lst, key=lambda item: item[2])
        a = sorted_data[-number_of_top_students-1:-1]
        a.reverse()
        s = list(map(lambda item:item[0], a))
        return s

res = get_top_performers('C:/Users/hopoghosyan/Desktop/HPHomework/Homework-session_5/data/students.csv', 3)
print(res)

def sorted_student_list(file_path):
    with open(file_path, newline = "") as f:
        lst = csv.reader(f, delimiter=",")
        sorted_data = sorted(lst, key=lambda item: item[1])
        sorted_data.reverse()
        with open("Sorted_by_age.csv", "w", encoding='UTF8') as new_f:
            writer = csv.writer(new_f)
            writer.writerows(sorted_data)

sorted_student_list('C:/Users/hopoghosyan/Desktop/HPHomework/Homework-session_5/data/students.csv')


