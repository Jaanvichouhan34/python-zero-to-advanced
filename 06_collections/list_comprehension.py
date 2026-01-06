# List Comprehension in Python

# Normal way
squares = []
for i in range(1, 6):
    squares.append(i * i)

print("Normal:", squares)

# List comprehension
squares_comp = [i * i for i in range(1, 6)]
print("List Comprehension:", squares_comp)
