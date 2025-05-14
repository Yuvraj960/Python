"""

Loops in Python:
1. For Loop: When you know the number of iterations in advance, use a for loop.
2. While Loop: When we know the condition to stop but not the number of iterations, use a while loop.

- In for loop we use range() function to iterate over a sequence of numbers.
- Range function can take 1, 2, or 3 arguments:
#   1. range(n): Generates numbers from 0 to n-1.
#   2. range(start, end): Generates numbers from start to end-1.
#   3. range(start, end, step): Generates numbers from start to end-1 with a step size.

- There is For else and While else loops also in Python.

Loop ending Statements:
1. break: Terminates the loop and transfers control to the statement following the loop.
2. continue: Skips the current iteration and continues with the next iteration.

"""

# For Loop

# Example 1: Print numbers from 0 to 9
for i in range(10):
    print(i, end=" ")
print()  # New line for better readability

# Example 2: Print even numbers from 0 to 20
for i in range(0, 21, 2):
    print(i, end=" ")
print()  # New line for better readability

# Example 3: Print numbers in list and at end print "Done"
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i, end=" ")
else:
    print("\nDone")

# Example 4: Print numbers from 1 to 10 and break when i is 5
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")

# Example 5: Print numbers from 1 to 10 and continue when i is 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")


# While Loop

# Example 1: Print numbers from 0 to 9
i = 0
while i < 10:
    print(i, end=" ")
    i += 1

# Example 2: Print even numbers from 0 to 20
i = 0
while i <= 20:
    print(i, end=" ")
    i += 2

# Example 3: Print numbers in list and at end print "Done"
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i], end=" ")
    i += 1
else:
    print("\nDone")

# Example 4: Print numbers from 1 to 10 and break when i is 5
i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1

# Example 5: Print numbers from 1 to 10 and continue when i is 5
i = 1
while i <= 10:
    if i == 5:
        continue
    print(i, end=" ")
    i += 1

