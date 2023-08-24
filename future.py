import time
from concurrent.futures import Future
from threading import Thread

def worker(x, y):
    print('About to work')
    time.sleep(20)
    print('Done')
    return x + y

# Wrapper around the function to use a future 
def do_work(x, y, fut):
    fut.set_result(worker(x, y))

def caller():
    fut = Future()
    Thread(target=do_work, args=(2, 3, fut)).start()
    result = fut.result()
    print('Got:', result)
