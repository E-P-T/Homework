
project_dir = '/home/python/code/epam/workingcopy/EpamPythonHomework/'
inputfile = project_dir + 'data/unsorted_names.txt'
outputfile = project_dir + 'data/sorted_names.txt'

def sort_file(src, dst):
    lines = []
    
    with open(src) as infile:
        for line in infile:
            lines.append(line)            
            
    lines.sort()
    
    with open(dst, 'w') as outfile:
        outfile.writelines(lines)
            

if __name__  == "__main__":
    sort_file(inputfile, outputfile)
    
