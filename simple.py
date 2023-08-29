# simple.py

# def add(x, y):
#     '''
#     Add x and y.
#     '''
#     # assert isinstance(x , int)
#     # assert isinstance(y, int)
#     return x + y

# Assertions are meant to check user inputs

# Should validate program invarients(internal conditions that must always hold true)

# Failure indicates a programming error and assign blame(e.g., to the caller)

# Can be disabled (python -O)


from validate import Integer, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x ** y


