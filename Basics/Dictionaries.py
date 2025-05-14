"""

Python Dictionaries have been used to store data values in key:value pairs.
A dictionary is:
    - Mutable
    - unordered
    - indexed
    - don't allows duplicate keys

Dictionaries are written with curly brackets, and they have keys and values.
If we have to initialize an empty dictionary:
    - my_dict = {}
    - my_dict = dict()

"""

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing items in a dictionary
print(my_dict["name"])  # Output: John
print(my_dict.get("age"))  # Output: 30

print(my_dict.get("age2"))  # Output: None (no error)
print(my_dict["age2"])  # Raises KeyError (error)

print(my_dict.items()) # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
print(my_dict.keys()) # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values()) # Output: dict_values(['John', 30, 'New York'])

# Adding items to a dictionary
my_dict["email"] = "hello@gmail.com"
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'hello@gmail.com'}

# Removing items from a dictionary
my_dict.pop("email")
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Dictionary Methods
print(my_dict.update({"age": 31}))  # Update the value of 'age' key
print(my_dict.clear())  # Clear the dictionary
print(my_dict.copy())  # Copy the dictionary
print(my_dict.fromkeys(["name", "age"], "unknown"))  # Create a new dictionary with default values
print(my_dict.popitem())  # Remove the last inserted key-value pair
print(my_dict.setdefault("name", "unknown"))  # Set default value for 'name' key
