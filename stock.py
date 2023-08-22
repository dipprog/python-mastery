# stock.py

class Stock:
    _types = (str, int, float)

    __slots__ = ('name', '_shares', '_price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
    
    @property 
    def shares(self):
        return self._shares
    
    @property 
    def price(self):
        return self._price
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected {self._types[1].__name__}')
        if value <  0:
            raise ValueError('shares must be >= 0')
        self._shares = value

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'Expected {self._types[2].__name__}')
        if value <  0:
            raise ValueError('price must be >= 0')
        self._price = value

    def sell(self, nshares):
        if nshares > 0 and nshares <= self.shares:
            self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

import csv
def read_portfolio(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)    # Skip headers
        for row in rows:
            records.append(Stock.from_row(row))
    return records

def print_portfolio(portfolio):
    headers = ['name', 'shares', 'price']
    print('%10s %10s %10s' % (headers[0], headers[1], headers[2]))
    print(('-' * 10 + ' ') * len(headers))
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


        
        