class FileWorker:
    def __init__(self, filename, mode = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except FileNotFoundError:
            print('Error: File not found')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


try:
    with FileWorker('../README.md', 'r') as file:
        for line in file:
            print(line)
    print(file.closed)
except:
    print('Error occured')
