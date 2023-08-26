# CLOSURE

# Function that returns another function
# def add(x, y):
#     def do_add():
#         print(f'{x} + {y} -> {x + y}')
#     return do_add

# Observe how the inner function refers to variables defined by the other function

# Futher observe that those variables are somehow kept alive after add() has finished.

# If an inner function is returned as a 'result', the inner function is known as a 'Closure'

# Essential feature: A "Closure" retains the values of all variables needed for the function to run properly later on.

# To make it work, references to the outer variables(bound variables) get carried along with the function.

# a = add(6, 7)
# print(a.__closure__)
# print(a.__closure__[0].cell_contents)
# print(a.__closure__[1].cell_contents)

# def sub(x, y):
#     result = x - y
#     def get_result():
#         return result
#     return get_result

# Closures only capture used variables
# Carefully observe: x and y are not included (not needded in the function body)

# def counter(n=0):
#     def incr():
#         nonlocal n
#         n += 1
#         return n
#     return incr

# Closure variables are mutable ( can be declared by nonlocal)
# Can be used to hold mutable internal state, much like object or class

def counter(value):
    def incr():
        nonlocal value
        value += 1
        return value
    def decr():
        nonlocal value
        value -= 1
        return value
    return incr, decr

# Above define two functions that manipulate a value




