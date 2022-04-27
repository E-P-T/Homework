# Task 4.1
# Implement a function which receives a string and replaces all " symbols with ' and vise versa.

def bracket_replace(line=""):
    result_line = ""
    for char in line:
        if (char == '"'):
             result_line+= "'"
        elif (char == "'"):
             result_line+= '"'
        else:
             result_line+= char
    print(result_line)


bracket_replace('''hello"" ' "' ''')
