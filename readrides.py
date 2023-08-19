# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dicts(filename):
    ''' 
    Read the bus ride data as a list of dicts
    '''
    records = RideData()    # <---- CHANGED
    with open(filename) as f:
        rows = csv.reader(f)
        heading = next(rows)    # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records

class Row:
    # Slot class, uncomment this to use slot
    # __slots__ = ('route', 'date', 'daytype', 'rides')
    def __init__(self, route, date, dattype, rides):
        self.route = route
        self.date = date
        self.daytype = dattype
        self.rides = rides

# Named Tuples, uncomment this to use named tuples
# from collections import namedtuple
# Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

def read_rides_as_instances(filename):
    ''' 
    Read the bus ride data as a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        heading = next(rows) # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)   # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(row[3])

    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

# The great "fake"
from collections.abc import Sequence
class RideData(Sequence):
    def __init__(self):
        # Each value is a list with all the values( a column)
        self.routes = []    # Columns
        self.dates = []
        self.dattypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        # If index is given as slice
        if isinstance(index, slice):
            new_self = self.__class__()
            new_self.routes = self.routes[index]
            new_self.dates = self.dates[index]
            new_self.dattypes = self.dattypes[index]
            new_self.numrides = self.numrides[index]
            return new_self
        return {
            'route': self.routes[index],
            'date': self.dates[index],
            'daytype': self.dattypes[index],
            'rides': self.numrides[index] }
         
    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.dattypes.append(d['daytype'])
        self.numrides.append(d['rides'])
    


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    read_rides = read_rides_as_dicts
    rows = read_rides('Data/ctabus.csv')

    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())

    # slot < tuple < namedtuple < class row < dict