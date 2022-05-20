"""
Task 7.4
Implement decorator for supressing exceptions. If exception not occure write log to console.
"""
from decorators import suppressor

fname = 'data/data.txt'


@suppressor
def main(path):
    with open(path, 'r') as inf:
        print(inf.read())


if __name__ == "__main__":
    main(fname)
