# reader.py

import csv
from abc import ABC, abstractmethod
from collections.abc import Sequence

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records
    
    @abstractmethod
    def make_record(self, headers, row):
        pass


class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }


class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
    

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


def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file with column type conversion
    '''
    parser = DictCSVParser(types)
    return parser.parse(filename)


def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)



            
        


    
