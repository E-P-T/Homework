"""
Implement class-based context manager for opening and working with file,
including handling exceptions. Do not use 'with open()'. Pass filename and mode via constructor.
"""

class OpenFile:
    # an instance of the OpenFile class if a fileobject
    def __init__(self, filename, mode):
        self.hand_file = open(filename, mode)

    def __enter__(self):
        return self.hand_file
    
    def __exit__(self, exception, value, trace):
        # the method prints the exception
        print(f'Resource.__exit__{(exception, value, trace)}')
        self.hand_file.close()
        return True

def main():
    with OpenFile("test.txt", 'w') as f:
        f.write("My")

    with OpenFile('demo.txt', 'w') as f:
        f.undefined_function()

if __name__ == '__main__':
    main()