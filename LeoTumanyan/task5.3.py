# ### Task 5.3
import pandas
# File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
# This file contains the student’s names, age and average mark.

# 1) Implement a function which receives file path and returns names of top performer students


def get_top_performers(file_path, number_of_top_students=5):
	df = pandas.read_csv(file_path)
	df.sort_values(["average mark"],
					ascending=[False],
					inplace=True)
	a = df['student name'].tolist()
	return [a[i] for i in range(number_of_top_students)]


# ```python
# def get_top_performers(file_path, number_of_top_students=5):
#     pass

# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
# ```

# 2) Implement a function which receives the file path with srudents info and writes CSV student information to the new file in descending order of age.
#    Result:


def arrange_by_age(file_path):
	df = pandas.read_csv(file_path)
	df.sort_values(['age'],
					ascending=[False],
					inplace=True, )
	df.to_csv('new.csv', index=False)


# ```
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27
# ```