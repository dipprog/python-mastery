# pcost.py

# total_cost = 0.0

# with open('Data/portfolio.dat', 'r') as f:
#     for line in f:
#         row = line.split()
#         nshares = int(row[1])
#         price = float(row[2])
#         total_cost += nshares * price
        

# print('Total Cost:', total_cost)


def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'r') as f:
        for line in f:
            row = line.split()
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except ValueError as e:
                print('Couldn\'t parse:', repr(line))
                print('Reason:', e)
                continue
        return total_cost
    
if __name__ == '__main__': 
    print(portfolio_cost('Data/portfolio.dat'))

    