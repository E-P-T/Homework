### Task 7.1
# TODO:Implement class-based context manager for opening and working with file, including handling exceptions. Do not
#  use 'with open()'. Pass filename and mode via constructor.

class FileManager:
    def __init__(self, file_path, mode):
        self.file = open(file_path, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


try:
    with FileManager('test.txt', 'ra') as fm:
        rd = fm.read()
except Exception as e:
    print(e)
else:
    print(rd)
