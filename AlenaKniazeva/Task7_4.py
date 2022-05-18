"""
Implement decorator for supressing exceptions. If exception not occure write log to console.
"""

import logging

logging.basicConfig(level=logging.INFO)

def ignore_excep(f):
    def wrapper (*args, **kwargs):
        try:
            res = f(*args, **kwargs)
            logging.info("No exception occur")
            return res
        except:
            logging.info("Exception suppressed")
            pass 
            
    return wrapper

@ ignore_excep
def div(x, y):
    return x/y


def main():
    div(6, 0)
    div(6, 2)

if __name__ == '__main__':
    main()