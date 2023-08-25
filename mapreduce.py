def map(func, values):
    result = []
    for x in values:
        result.append(func(x))
    return result

def reduce(func, values, initial=0):
    result = initial
    for x in values:
        result = func(x, result)
    return result

def sum(x, y):
    return x + y

def square(x):
    return x * x

nums = [1, 2, 3, 4]

result = reduce(sum, map(square, nums))