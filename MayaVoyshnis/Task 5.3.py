'''
File data/students.csv stores information about students in CSV format.
This file contains the student’s names, age and average mark.


Implement a function which receives file path and returns names of top performer students
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))
>>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
Implement a function which receives the file path with srudents info and writes CSV student information to the new file in descending order of age. Result:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
'''
def get_top_performers(file_path,number_of_top_students=5):
    lst=list(map(lambda line:line.replace('\n','').split(','),open(file_path)))
    lst.pop(0)
    lst.sort(key=lambda x:float(x[2]))
    return list(map(lambda x:x[0],lst[-1:-1*(number_of_top_students+1):-1]))


if __name__ == '__main__':
    print(get_top_performers("/repositories/HomeTask/data/students.csv"))
