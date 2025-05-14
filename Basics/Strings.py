# Strings are immutable sequences of characters

a = 'hello' # single quoted string
b = "hello" # double quoted string
c = '''hello''' # triple single quoted string


# String Slicing

print(a[0]) # prints 'h'
print(a[1]) # prints 'e'
print(a[-1]) # prints 'o'
print(a[-2]) # prints 'l'

print(a[2:5]) # prints 'llo'
print(a[0:5]) # prints 'hello'

print(a[:5]) # prints 'hello'
print(a[2:]) # prints 'llo'

print(a[2:5:2]) # prints 'l'
print(a[::2]) # prints 'hlo'

print(a[::-1]) # prints 'olleh'


# String Methods

print(len(a)) # prints the length of the string
print(a.startswith("he")) # Checks if the string starts with 'he'
print(a.endswith("lo")) # Checks if the string ends with 'lo'
print(a.split()) # Splits the string into a list of words
print(a.replace('l', 'L')) # Replaces 'l' with 'L'
print(a.count('l')) # Counts the number of occurrences of 'l' in the string
print(a.find('l')) # Returns the index of the first occurrence of 'l'
print(a.capitalize()) # Capitalizes the first letter of the string
print(a.title()) # Capitalizes the first letter of each word in the string
print(a.upper()) # Converts the string to uppercase
print(a.lower()) # Converts the string to lowercase
print(a.swapcase()) # Swaps the case of each letter in the string
print(a.strip()) # Removes leading and trailing whitespace from the string
