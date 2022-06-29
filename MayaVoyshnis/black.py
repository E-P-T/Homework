import time

def timer(f):
    def wrapper(sec):
        t0=time.time()
        res=f(sec)
        t1=time.time()
        print(f'Function execution  time: {t1-t0:.2f}')
        return res
    return wrapper

@timer
def sleeper(sec):
    time.sleep(sec)

sleeper(5)