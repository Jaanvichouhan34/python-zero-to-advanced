# Exception Handling in Python

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Please enter valid integers")

except Exception as e:
    print("Unexpected error:", e)

else:
    print("Calculation successful")

finally:
    print("Program execution completed")
