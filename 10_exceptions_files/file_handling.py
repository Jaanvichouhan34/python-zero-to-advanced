# File Handling in Python

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is Python file handling.\n")
    file.write("Learning Python is fun!")

print("File written successfully")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile content:")
    print(content)
