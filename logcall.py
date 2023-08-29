# logcall.py

from functools import wraps

# def logged(func):
#     print('Adding logged to', func.__name__)
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Calling', func.__name__)
#         return func(*args, **kwargs)
#     return wrapper


def logformat(fmt):
    def logged(func):
        print('Adding logged to', func.__name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged