"""

Recursion is basically defined as a function that calls itself.
Recursion is a powerful concept in programming that allows a function to call itself in order to solve a problem.
It is often used to solve problems that can be broken down into smaller, similar subproblems.
It is done so because the solution to the problem can be expressed in terms of the solution to smaller instances of the same problem.

For Example:
1. Factorial of a number: The factorial of a number n is the product of all positive integers less than or equal to n. It can be defined recursively as:
   - factorial(n) = n * factorial(n-1) for n > 0
   - factorial(0) = 1 (base case)
   - factorial(1) = 1 (base case)
   - factorial(2) = 2 * factorial(1) = 2 * 1 = 2
   - factorial(3) = 3 * factorial(2) = 3 * 2 = 6
   - And so on...
   In this case, the base case is when n is 0 or 1, where the factorial is defined to be 1. And the recursive case
   is when n is greater than 1, where the factorial is defined in terms of the factorial of n-1.

2. Fibonacci series: The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones.
    It can be defined recursively as:
    - fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 1
    - fibonacci(0) = 0 (base case)
    - fibonacci(1) = 1 (base case)
    - fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1
    - fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
    - And so on...
    In this case, the base cases are when n is 0 or 1, where the Fibonacci number is defined to be 0 or 1 respectively.
    And the recursive case is when n is greater than 1, where the Fibonacci number is defined in terms of the Fibonacci numbers of n-1 and n-2.
"""

# Factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Fibonacci series using recursion
def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case