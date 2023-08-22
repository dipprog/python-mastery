# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file with column type conversion
    '''
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {name: func(val) for name, func, val in zip(headers, types, row)}
            records.append(record)

    return records

from collections.abc import Sequence
class DataCollection(Sequence):
    def __init__(self, headers):
        for col_name in headers:
            setattr(self, col_name, [])
        self.headers = headers
    
    def __len__(self):
        return len(getattr(self, self.headers[0]))
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            new_self = self.__class__(self.headers)
            for col_name in self.headers:
                setattr(new_self, col_name, getattr(self, col_name)[index])
            return new_self
        
        data = {col_name:getattr(self, col_name)[index] for col_name in self.headers}
        return data
    
    def append(self, d):
        for col_name in self.headers:
            getattr(self, col_name).append(d[col_name])


def read_csv_as_columns(filename, types):
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        data = DataCollection(headers)
        for row in rows:
            record = {name:func(val) for name, func, val in zip(headers, types, row)}
            data.append(record)

    return data

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records



            
        


    
