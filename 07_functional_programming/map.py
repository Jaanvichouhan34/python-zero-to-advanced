# map() function in Python

# map() applies a function to each item in an iterable

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

result = map(square, numbers)

print("Squares using map:", list(result))

# Using lambda with map
double = map(lambda x: x * 2, numbers)
print("Double using lambda:", list(double))
