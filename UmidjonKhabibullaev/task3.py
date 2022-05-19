import pandas as pd


def get_top_performers(file_path, number_of_top_students = 5):
    """ Function to find the top performer students (by means of average marks)
        in a file located in `file_path`.
        Returns the list of such students
    """
    df = pd.read_csv(file_path) # create a pandas DF
    df = df.drop(columns=["age"], axis=0) # Remove "age" column since we don't need it
    df = df.sort_values(by=["average mark"], ascending=False) # sort by average mark in descending order
    
    return list(df.head(number_of_top_students)["student name"])


def sort_students_by_age(file_path):
    """ Function that receives a file path to students data containing name, age, average mark.
        Sorts the table by age in decsending order, writes the result to a new file.
    """
    df = pd.read_csv(file_path)
    df = df.sort_values(by=["age"], ascending=False)
    df.to_csv("sorted_students.csv", index=False)


if __name__ == "__main__":
    print(get_top_performers("../data/students.csv"))
    sort_students_by_age("../data/students.csv")