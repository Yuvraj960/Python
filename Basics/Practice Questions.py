# ===========================================================
# SOME QUESTION PRACTICE
# ===========================================================

# Write program to add 2 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print("The sum of", a, "and", b, "is:", sum)


# Write program to find the remainder of a number when divided by z
a = int(input("Enter a number: "))
z = int(input("Enter a divisor: "))
remainder = a % z
print("The remainder of", a, "when divided by", z, "is:", remainder)


# Write program to find average of 2 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
average = (a + b) / 2
print("The average of", a, "and", b, "is:", average)


# Program to find the square of a number
a = int(input("Enter a number: "))
square = a ** 2
print("The square of", a, "is:", square)


# Create list of 7 fruints by user input
fruits = []
for i in range(7):
    fruits.append(input("Enter a fruit: "))
print("The list of fruits is:", fruits)


# Find largest number from 4 user input numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if(num1 >= num2) and (num1 >= num3) and (num1 >= num4):
    largest = num1
elif(num2 >= num1) and (num2 >= num3) and (num2 >= num4):
    largest = num2
elif(num3 >= num1) and (num3 >= num2) and (num3 >= num4):
    largest = num3
else:
    largest = num4
print("The largest number is", largest)


# Interview question: Find the length of the set
my_set = set()
my_set.add(1)
my_set.add(1.0)
my_set.add("1")
print(len(my_set)) # Output: 2 (1 and 1.0 are considered the same, but "1" is a different type)


# Find Given no. is prime or not
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num/2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")


# Generate following pattern
#   *
#  ***
# *****

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")

# Generate pattern:
# *
# ***
# ****

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    print("*" * (2*i-1), end="")
    print("")

# Generate pattern:
# ***
# * *
# ***

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")