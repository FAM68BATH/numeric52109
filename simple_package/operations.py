###
## simple_package - Module operations.py
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##
## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b

if __name__ == "__main__":
    print('Welcome to the Basic Online Calculator')
    print('The following operations are available at the moment:')
    operations = {'Addition': add,
                  'Subtraction': subtract,
                  'Multiplication': multiply,
                  'Division': divide}

    for i in range(len(operations)):
        print(f"{i+1}. {operations[i]}")

    # Display available options
print("Available operations:")
for operation in operations.keys():
    print(f"  - {operation}")

# Get user input
user_choice = input("\nEnter operation: ").strip().lower()

if user_choice in operations:
    # Get numbers from user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Call the function using the dictionary
        result = operations[user_choice](num1, num2)
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers!")
else:
    print("Invalid operation!")

    
    