# stock.py
import validate

class Stock:
    _types = (str, int, float)

    __slots__ = ('name', '_shares', '_price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
    
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == (other.name, other.shares, other.price))

    @property
    def cost(self):
        return self.shares * self.price
    
    @property 
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value):
        self._shares = validate.PositiveInteger.check(value)

    @property 
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = validate.PositiveFloat.check(value)

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


        
        