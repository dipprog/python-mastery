# reader.py

import csv
from collections.abc import Sequence
from stock import Stock
import logging

logging.basicConfig(level=logging.DEBUG, filename='reader.log')
log = logging.getLogger(__name__)



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

from typing import Iterable

def convert_csv(lines: Iterable, converter_func, *, headers: list|None = None) -> list:
    '''
    Convert lines of CSV data into a list of container defined by converter_func
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    records = []
    for rowno, row in enumerate(rows, start=1):
        try:
            record = converter_func(headers, row)
            records.append(record)
        except ValueError as e:
            # print(f"Row {rowno}: Bad row: {repr(row)}")
            log.warning(f"Row {rowno}: Bad row: {repr(row)}")
            # log.warning('Row %s: Bad row: %s', rowno, row)
            # print(f"Error: {e}")
            log.debug(f"Row {rowno}: Reason: {repr(row)}")
            continue
    return records

def csv_as_dicts(lines: Iterable, types: list, *, headers:list|None = None) ->list[dict]:
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    return convert_csv(lines, lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row)}, headers=headers)
            
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    return convert_csv(lines, lambda headers, row: cls.from_row(row),headers=headers)
        
def read_csv_as_dicts(filename: str, types: list, *, headers: list|None = None) -> list[dict]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename, 'rt') as file:
        return csv_as_dicts(file, types, headers=headers)
    
def read_csv_as_instances(filename: str, cls: Stock, *, headers: list|None = None) -> list[Stock]:
    '''
    Read a CSV data into a list of instances
    '''
    with open(filename, 'rt') as file:
        return csv_as_instances(file, cls, headers=headers)
    


    
