from contextlib import contextmanager

@contextmanager
def openFile(filename, mode = 'r'):
    file = None
    try:
        file = open(filename, mode)                             
        yield file
    except FileNotFoundError:
        print('Error: File not found')
    if file:
        file.close()

try:
    with openFile('../README.md', 'r') as file:
        for line in file:
            print(line)
    print(file.closed)
except:
    print('Error occured')
