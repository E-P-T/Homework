# Task 5.3
# File `data/students.csv` stores information about students in
# [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
# This file contains the student’s names, age and average mark.
# 1) Implement a function which receives file path and returns names of top performer students
# ```python
# def get_top_performers(file_path, number_of_top_students=5):
#     pass

# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
# ```

# 2) Implement a function which receives the file path with students info and writes CSV student information
# to the new file in descending order of age.
# Result:
# ```
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27


def get_top_performers(file_path="data/students.csv", number_of_top_students=5):
    with open(file_path, mode='r') as file:
        result = list(file)
    result = [x[:-1:].split(',') for x in result][1:]
    for i in range(len(result)):
        for j in range(len(result[i])):
            if j == 1:
                result[i][j] = int(result[i][j])
            elif j == 2:
                result[i][j] = float(result[i][j])
    result = sorted(result, key=lambda x: x[2], reverse=True)
    result = result[:number_of_top_students]

    result_names = []
    for i in result:
        result_names.append(i[0])

    return result_names


# test
# print(get_top_performers())


def get_top_aged_students():
    with open("data/students.csv", mode='r') as file:
        result = list(file)
    result = [x[:-1:].split(',') for x in result][1:]

    for i in range(len(result)):
        for j in range(len(result[i])):
            if j == 1:
                result[i][j] = int(result[i][j])
    result = sorted(result, key=lambda x: x[1], reverse=True)

    for i in range(len(result)):
        for j in range(len(result[i])):
            if j == 1:
                result[i][j] = str(result[i][j])

    for i in range(len(result)):
        result[i] = ','.join(result[i])

    result = '\n'.join(result)
    result = 'student name,age,average mark\n' + result

    with open("data/students_sorted_by_age.csv", mode='w') as file:
        file.write(result)

    return result

# test
# get_top_aged_students()
