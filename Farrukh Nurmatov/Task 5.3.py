"""File `data/students.csv` stores information about students in
[CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
This file contains the student’s names, age and average mark.
1) Implement a function which receives file path and returns names of top performer students
2) Implement a function which receives the file path with students info and writes CSV
student information to the new file in descending order of age.
"""

def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, "r") as file:
        head = file.readline()
        stud_db = []
        for line in file:
            str_lst = line.split(",")
            stud_lst = [str_lst[0], int(str_lst[1]), float(str_lst[2])]
            stud_db.append(stud_lst)
        stud_db.sort(key=lambda x:x[2], reverse=True)
        top_performers = [stud[0] for stud in stud_db[:number_of_top_students]]
        return top_performers


def descending_age(in_filepath, out_filepath):
    with open(in_filepath, "r") as read_file,\
            open(out_filepath, "w") as write_file:
        head = read_file.readline()
        stud_db = []
        for line in read_file:
            str_lst = line.split(",")
            stud_lst = [str_lst[0], int(str_lst[1]), float(str_lst[2])]
            stud_db.append(stud_lst)
        stud_db.sort(key=lambda x: x[1], reverse=True)
        write_file.write(head)
        for stud in stud_db:
            write_file.write(",".join([stud[0], str(stud[1]), str(stud[2])]) + "\n")


if __name__ == '__main__':
    print(get_top_performers("data/students.csv"))
    print(descending_age("data/students.csv", "data/sorted_students.csv"))