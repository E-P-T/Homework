class CustomFileHandling:
    """ Custom Context Manager Class to handle basic file operations. """

    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode


    def readable(self):
        return self.f.readable()
    
    def writable(self):
        return self.f.writable()

    def read(self, number_of_chars: int = None):
        return "----------- Reading a file... ---------------\n" + self.f.read(number_of_chars) + "\n--------------------------------------------"
    
    def readlines(self, number_of_lines: int = -1):
        l = self.f.readlines(number_of_lines)
        return l

    def readline(self, number_of_bytes: int = -1):
        line = self.f.readline(number_of_bytes)
        return line

    def write(self, s: str):
        n = self.f.write(s)
        return n
    
    def writeline(self, lines: list[str]):
        self.f.writelines(lines)
    
    def open_file(self):
        print("Opening a file ...")
        self.f = open(self.filename, self.mode)

    def close_file(self):
        print("Closing a file...")
        self.f.close()
    

    def __enter__(self):
        print("File handling has started!")
        self.f = open(self.filename, self.mode)
        # self.open_file()
        return self.f
    
    def __exit__(self, exception, value, trace):
        if exception:
            print(f"{exception}\n{value}\n{trace}")        
    
        self.f.close()


with CustomFileHandling("task.txt", "r") as f:
    if not f.writable():

        v = f.seek(3)
        print(v)
    