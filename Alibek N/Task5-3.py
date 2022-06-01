import os

path_input = os.getcwd().rstrip('\Alibek N') + '\data' +  '\\' + 'students.csv'

def get_top_performers(path_input, number_of_top_students=5):
    students = {}
    answer = []
    with open(path_input) as file:
        for st in file:
            line = st.strip('\n').split(',')
            students[line[0]] = line[2]
    file.close()
    del students['student name']
    students = sorted(students.items(), key=lambda x: x[1], reverse=True)
    for info in students:
        answer.append(info[0])
    return answer[:number_of_top_students]

print(get_top_performers(path_input))




