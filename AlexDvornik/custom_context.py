from time import sleep
import io


class File:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        print("[+] Initializing file object...")
        sleep(1)

    def __enter__(self):
        try:
            self.file_object = open(self.file_path, self.mode)
        except FileNotFoundError as err:
            print(err)
        else:
            print("[+] Opening file object...")
            sleep(1)
            return self.file_object

    def read(self):
        return self.file_object.readline()

    def write(self, s: str):
        return self.file_object.write(s)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[+] Closing context manager...")
        if isinstance(exc_val, (FileNotFoundError, AttributeError, io.UnsupportedOperation)):
            print(f"[+] An exception occurred in your with block: {exc_type}")
            print(f"    An exception message: {exc_val}")
            return True
