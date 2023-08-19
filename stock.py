# stock.py

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        if nshares > 0 and nshares < self.shares:
            self.shares -= nshares

import csv
def read_portfolio(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)    # Skip headers
        for row in rows:
            records.append( Stock( str(row[0]), int(row[1]),float(row[2]) ) )
    return records

def print_portfolio(portfolio):
    headers = ['name', 'shares', 'price']
    print('%10s %10s %10s' % (headers[0], headers[1], headers[2]))
    print(('-' * 10 + ' ') * len(headers))
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


        
        