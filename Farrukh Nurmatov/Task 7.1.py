"""Implement class-based context manager for opening and working with file, including handling exceptions.
Do not use 'with open()'. Pass filename and mode via constructor."""
from os.path import exists


class FileNotExists(Exception):
    pass


class IncorrectMode(Exception):
    pass


class MyFile:
    modes = ["w", "r", "b", "x", "a", "t", "+"]

    def __init__(self, filename, mode):
        try:
            if not exists(filename):
                raise FileNotExists
            if mode not in self.modes:
                raise IncorrectMode
        except FileNotExists:
            print(f"File {filename} doesn't exist.")
        except IncorrectMode:
            print(f"{mode} incorrect mode.")
        else:
            print("MyFile created for file {} with mode {}".format(filename, mode))
            self.filename = filename
            self.mode = mode

    def open(self):
        print(f"File {self.filename} is opened")
        self.file = open(self.filename, self.mode)

    def close(self):
        print(f"File {self.filename} is closed")
        self.filename.close()


if __name__ == '__main__':
    a = MyFile("data/file.txt", "r")
    a.open()
    a.close()
