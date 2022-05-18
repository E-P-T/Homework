"""
Implement a generator which will generate odd numbers endlessly.
"""

def endless_generator():
    num = 1
    while True:
        yield num
        num +=2

if __name__ == "__main__":
    gen = endless_generator()
    while True:
        print(next(gen))