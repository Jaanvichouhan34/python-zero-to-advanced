# break and continue in Python

# break example
for i in range(1, 10):
    if i == 5:
        break
    print("Before break:", i)

print()

# continue example
for i in range(1, 6):
    if i == 3:
        continue
    print("After continue:", i)
