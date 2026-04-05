# Level 3: Simple CLI Calculator
# Functions for operations
def add(a, b):
    return a + b  # addition
def subtract(a, b):
    return a - b  # subtraction
def multiply(a, b):
    return a * b  # multiplication
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"  # error check
    return a / b
# Show menu
print("Simple Calculator")
print("+  -  *  /")
# Loop to keep calculator running
while True:
    op = input("Choose operation (or q to quit): ")
    if op == "q":
        break  # stop program
    # Take numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    # Check operation and call function
    if op == "+":
        print("Result:", add(num1, num2))
    elif op == "-":
        print("Result:", subtract(num1, num2))
    elif op == "*":
        print("Result:", multiply(num1, num2))
    elif op == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation")