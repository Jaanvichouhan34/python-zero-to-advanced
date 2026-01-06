# Function Basics in Python

def greet():
    print("Hello, welcome to Python!")

greet()

print()

# Function with parameters
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

print()

# Function with default parameter
def introduce(name, course="Python"):
    print("Name:", name)
    print("Course:", course)

introduce("Jaanvi")
introduce("Jaanvi", "Java")
