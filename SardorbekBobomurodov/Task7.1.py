class OpenFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except Exception as error:
            print(error)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


if __name__ == "__main__":
    with OpenFile("sample.txt", "r") as file:
        file.write("Go")

    print(file.closed)
