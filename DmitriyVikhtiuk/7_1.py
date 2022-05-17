class FileManager(object):
    def __init__(self, path, mode):
        self.file_obj = open(path, mode)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        if exc_val:
            raise exc_val


with FileManager("test.txt", 'a') as f:
    f.write("Hello!")