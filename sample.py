# sample.py

from logcall import logformat


logged = logformat('{func.__code__.co_filename}:{func.__name__}')

@logged
def mul(x,y):
    return x * y

class Spam:
    @logged
    def instance_method(self):
        pass

    @classmethod
    @logged
    def class_method(cls):
        pass

    @staticmethod
    @logged
    def static_method():
        pass

    @property
    @logged
    def property_method(self):
        pass