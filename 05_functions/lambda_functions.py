# Lambda Functions in Python

# Normal function
def square(x):
    return x * x

print("Square:", square(5))

# Lambda function
square_lambda = lambda x: x * x
print("Square using lambda:", square_lambda(6))

# Lambda with multiple arguments
add = lambda a, b: a + b
print("Addition:", add(10, 20))
