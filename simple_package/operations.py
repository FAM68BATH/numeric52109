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
    operations = ['Addition', 'Subtraction', 'Multiplication', 'Division']
    for i in range(len(operations)):
        print(f"{i+1}. {operations[i]}")
    op = int(input(f"Enter you choice(1-{i+1}): "))
    if (op<1 or op>i+1):
        print('Invalid input! The calculator will now close. Please try again.')
        exit()
    else:
        print(op)
    