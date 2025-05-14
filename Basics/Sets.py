"""

Sets in Python:
- Sets are used to store multiple items in a single variable.
- Sets are:
    - immutable
    - Unordered
    - Unindexed
    - Don't allow duplicate values

Sets are written with curly brackets.
For creating an empty set:
    - my_set = set()

    =================
    WARNING
    =================
    - my_set = {} # This creates an empty dictionary, not a set.

"""

my_set = {"apple", "banana", "cherry"}
print(type(my_set))  # Output: <class 'set'>
print(len(my_set))  # Output: 3
print("banana" in my_set)  # Output: True
print(my_set.add("orange"))  # Add an item to the set
print(my_set.remove("banana"))  # Remove an item from the set
print(my_set.discard("banana"))  # Discard an item from the set (no error if not found)
print(my_set.pop())  # Remove a random item from the set
print(my_set.clear())  # Clear the set
print(my_set.copy())  # Copy the set
print(my_set.union({"kiwi", "mango"}))  # Union of two sets
print(my_set.intersection({"kiwi", "mango"}))  # Intersection of two sets
print(my_set.difference({"kiwi", "mango"}))  # Difference of two sets
print(my_set.issubset({"apple", "banana", "cherry", "kiwi", "mango"}))  # Check if a set is a subset of another set
print(my_set.issuperset({"apple", "banana"}))  # Check if a set is a superset of another set