# filter() function in Python

# filter() selects elements based on a condition

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(x):
    return x % 2 == 0

even_numbers = filter(is_even, numbers)

print("Even numbers:", list(even_numbers))

# Using lambda with filter
odd_numbers = filter(lambda x: x % 2 != 0, numbers)
print("Odd numbers:", list(odd_numbers))
