"""

File Handling in Python

File handling is a critical aspect of programming, allowing you to read from and write to files on your system.
Python provides built-in functions and methods for file operations, making it easy to work with files.

Opening a File
The open() function is used to open a file in Python. It takes two arguments: the file name and the mode.
Modes:
'r' - Read (default mode)
'w' - Write (overwrites the file)
'a' - Append (adds to the end of the file)
'b' - Binary mode
't' - Text mode (default mode)
'r+' - Read and write
'w+' - Write and read (overwrites the file)
'a+' - Append and read
'b+' - Binary read and write
't+' - Text read and write
'rb' - Read binary
'wb' - Write binary
'ab' - Append binary

"""

# Opening a file in read mode
file = open("example.txt", "r")
# Reading the contents of the file
content = file.read()
print(content)
# Closing the file
file.close()

# Opening a file in write mode
file = open("example.txt", "w")
# Writing to the file
file.write("Hello, World!")
# Closing the file
file.close()

# Opening a file in append mode
file = open("example.txt", "a")
# Appending to the file
file.write("\nThis is an appended line.")
# Closing the file
file.close()

# Reading a file line by line can also be done using a with statement

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes leading/trailing whitespace
# The with statement automatically closes the file after the block is executed

