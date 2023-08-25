def sum_squares(nums):
    total = 0
    for n in nums:
        total += n ** 2
    return total

def sum_cubes(nums):
    total = 0
    for n in nums:
        total += n ** 3
    return total


def sum_map(func, nums):
    total = 0
    for n in nums:
        total += func(n)
    return total

def square(x):
    return x * x

# Lambda function - Anonymous function on the spot
nums = [1,2,3,4]
r = sum_map(lambda x: x*x, nums)