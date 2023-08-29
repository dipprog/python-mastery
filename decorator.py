# A decorator is a function that creates a wrapper around another function

# The warpper is a new function that works exactly like the original function(same arguments, same return type) except that some kind of extra processing is carried out

def add(x, y):
    return x + y

def logged(func):
    # Define a wrapper function around func
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

# When we create a wrapper, we often want to replace the original function with it

# Other codes continues to use the original function name, but it is unaware that a wrapper has been injected(that's the whole point)

# When we replace a function with a wrapper, we are usually giving the function extra functionality. This process is known as 'decoration'. We are 'decorating' a function with some extra features.

# Whenever we see a decorader syntax, just remember that a function is getting wrapped.

# A decorator that reports execution time
from functools import wraps
import time
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return r
    return wrapper

@timethis
def check():
    '''
    List creation
    '''
    l = []
    for i in range(10000000):
        l.append(i)


# Decorator with Args
# Logging with a custom message
def logmsg(message):
    def logged(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(message.format(name=func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return logged

