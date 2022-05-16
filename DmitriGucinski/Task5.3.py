import csv

def get_top_performers(file_path, number_of_top_students=5):
    '''Receives file path and returns names of top performer students'''
    with open(file_path) as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        rows = [row for row in csvreader]
        
    rows = sorted(rows, key=lambda item: float(item[2]), reverse=True)
    
    return [row[0] for row in rows[:number_of_top_students]]
                        
    

def create_ordered_file(file_path, outputfile, reverse=True):
    '''Receives the file path with students info and writes CSV student information to the new file in descending order of age.'''
    with open(file_path) as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        rows = [row for row in csvreader]
        
    rows = sorted(rows, key=lambda item: int(item[1]), reverse=reverse)
    
    with open(outputfile, 'w') as outfile:
        csvwriter = csv.writer(outfile, delimiter = ',')
        csvwriter.writerow(header)
        csvwriter.writerows(rows)


if __name__ == "__main__":
    data_path = '/home/python/code/epam/workingcopy/EpamPythonHomework/data/'
    inputfile = data_path + "students.csv"
    outputfile = data_path + "students_ordered.csv"
    
    print(get_top_performers(inputfile))
    create_ordered_file(inputfile, outputfile)
