# Task 7.1
# Implement class-based context manager for opening
# and working with file, including handling exceptions. Do not use 'with open()'.
# Pass filename and mode via constructor.


class MyFileContextManager:
    mode_chars = ('r', 'w', 'x', 'a', 'b', 't', '+', 'U')

    def __init__(self, file_path, mode: str):
        print("init")
        self.file = open(file_path, mode)

    def __enter__(self):
        print("enter")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        self.file.close()


try:
    with MyFileContextManager(".\\data\\Task1_sorted_name.txt", 'rrr') as fileContext:
        fileContext.write("qwwr")
except Exception as e:
    print(e)
