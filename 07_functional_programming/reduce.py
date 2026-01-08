# reduce() function in Python

from functools import reduce

# reduce() applies a rolling computation

numbers = [1, 2, 3, 4, 5]

def add(a, b):
    return a + b

total = reduce(add, numbers)
print("Sum using reduce:", total)

# Using lambda with reduce
product = reduce(lambda a, b: a * b, numbers)
print("Product using lambda:", product)
