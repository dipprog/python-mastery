# reader.py

import csv
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
        records = DataCollection(headers)
        for row in rows:
            record = {name:func(val) for name, func, val in zip(headers, types, row)}
            records.append(record)

    return records


def convert_csv(lines, converter_func, *, headers=None):
    '''
    Convert lines of CSV data into a list of container defined by converter_func
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    return list(map(lambda row: converter_func(headers, row), rows))


def csv_as_dicts(lines, types, *, headers = None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    return convert_csv(lines, lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row)}, headers=headers)
            
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    return convert_csv(lines, lambda headers, row: cls.from_row(row),headers=headers)
        

def read_csv_as_dicts(filename, types, *, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename, 'rt') as file:
        return csv_as_dicts(file, types, headers=headers)
    

def read_csv_as_instances(filename, cls, *, headers=None):
    '''
    Read a CSV data into a list of instances
    '''
    with open(filename, 'rt') as file:
        return csv_as_instances(file, cls, headers=headers)
    


    
