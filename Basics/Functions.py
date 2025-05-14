"""

Functions in Python are used to encapsulate code into reusable blocks.
Functions can take parameters and return values.
Functions can be defined using the 'def' keyword followed by the function name and parentheses.

There are two types of functions:
1. Built-in functions: These are pre-defined functions provided by Python, such as print(), len(), etc.
2. User-defined functions: These are functions defined by the user to perform specific tasks.

We can define 4 types of functions:
1. Function with no parameters and no return value
2. Function with no parameters and return value
3. Function with parameters and no return value
4. Function with parameters and return value

"""

# Function with no parameters, no return value
def avg(): # Function definition
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    average = (a + b + c) / 3
    print("The average of", a, ",", b, "and", c, "is:", average)

# Function call
avg()

# Function with parameters, no return value
def greet(name):
    print("Hello", name, "! Have a great day!")

greet("John")

# Function with no parameters, return value
def square():
    a = int(input("Enter a number: "))
    return a ** 2

ans = square()
print("The square of the number is:", ans)

# Function with parameters, return value
def add(a, b):
    return a + b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
ans = add(a, b)
print("The sum of", a, "and", b, "is:", ans)


# Function with default parameters
def greet(name, message="Hello"):
    print(message, name, "! Have a great day!")

greet("John")  # Uses default message
greet("John", "Welcome")  # Uses custom message