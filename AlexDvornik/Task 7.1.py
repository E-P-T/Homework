"""
Task 7.1
Implement class-based context manager for opening and working with file, including handling exceptions.
Do not use 'with open()'. Pass filename and mode via constructor.

"""
from custom_context import File

with File('data/data.txt', "w") as file:
    file.write("text" + '\n')
