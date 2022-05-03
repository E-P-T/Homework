""" This program contains the next functions:
1) A function which receives CSV file path with the information about students
 and returns names of top performer students
2) a function which receives the file path with students info and writes
 CSV student information to the new file in descending order of age
"""

import pandas as pd

def get_top_performers(file_path, number_of_top_students=5):
    stud = pd.read_csv(file_path, header = 0, sep = ',')
    sorted_stud = stud.sort_values(by='average mark', ascending=False,ignore_index=True)
    res=[]
    for i in range(0,number_of_top_students+1):
        res.append(sorted_stud.loc[i]['student name'])
    return(res)

def sort_by_age(file_path):
    stud = pd.read_csv(file_path, header = 0, sep = ',')
    sorted_stud = stud.sort_values(by='age', ascending=False,ignore_index=True)
    sorted_stud.to_csv('sorted_stud.csv', index=False)

if __name__ == "__main__":
    file_path = input("Enter a path to datafile: ")
    num_stud = int(input("Enter the required number of top students:"))
    print("Top performers are: {}".format(get_top_performers(file_path, num_stud)))
    sort_by_age(file_path)
