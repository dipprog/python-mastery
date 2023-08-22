# date.py

import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '%d-%d-%d' % (self.year, self.month, self.day)
    
    def __repr__(self):
        return 'Date(%r,%r,%r)' % (self.year, self.month, self.day)
    
    @classmethod
    def today(cls):
        t = time.localtime()
        self = cls.__new__(cls)
        self.year = t.tm_year
        self.month = t.tm_mon
        self.day = t.tm_mday
        return self
    
class Manager:
    def __enter__(self):
        print('Enterning...')
        return self
    
    def __exit__(self, ty, val, tb):
        print('Leaving...')
        if ty:
            print('An exception occurred.')

            
