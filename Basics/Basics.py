# Single-line comment

"""
Mutli
line
comment
"""

# Printing in Python

print("Hello World")



# =====================
# SOME BASIC QUESTIONS
# =====================

# Write a poem (mutli-line string)

print('''
Roses are red,
Violets are blue,
I am a programmer,
I love to code too.
''')


# Print table of 5 using loop

# Using a for loop
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Using a while loop
i = 1
while i <= 10:
    print(f"5 x {i} = {5 * i}")
    i += 1


# Write a python Program to print contents of the directory using the OS module

import os
dirpath = "/" # Change this to the directory you want to list. This is the root directory (C:\).
contents = os.listdir(dirpath)
for item in contents:
    print(item)
