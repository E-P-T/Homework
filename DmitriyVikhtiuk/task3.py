import pandas
import pandas as pd


def get_top_performers(file_path, number_of_top_students=5):
    count = 0
    leaders = []
    p = pandas.read_csv(file_path)
    d = {row["student name"]: row["average mark"] for item, row in p.iterrows()}
    while count < number_of_top_students:
        for key, value in d.items():
            if d[key] == max(d.values()):
                leaders.append(key)
                d.pop(key)
                break
        count += 1
    return leaders


def get_new_csv(file_path):
    p = pandas.read_csv(file_path)
    list_of_tup = [(row["student name"], row["age"], row["average mark"])for item, row in p.iterrows()]
    list_of_tup.sort(key=lambda x: x[1], reverse=True)
    data = pandas.DataFrame(data=list_of_tup, columns=["student name", "age", "average mark"])
    data.to_csv("new_csv.csv", index=False)




print(get_top_performers("students.csv"))
get_new_csv("students.csv")