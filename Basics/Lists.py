"""

Lists are the most versatile data structure in Python.
They can hold any type of data and they are mutable, meaning you can change their contents after creation.

"""

friends = ["Alice", "Bob", "Charlie", 7, 3.4, True, None]
print(type(friends)) # <class 'list'>

# List Indexing
# List has almost the same indexing as strings.

print(friends[0])  # First element
print(friends[1])  # Second element
print(friends[-1])  # Last element
print(friends[-2])  # Second to last element
print(friends[1:4])  # Slice from index 1 to 3 (4 is not included)
print(friends[:3])  # Slice from start to index 2 (3 is not included)


# List Methods

# Append
friends.append("David")  # Add David to the end of the list

# Insert
friends.insert(1, "Eve")  # Insert Eve at index 1

# Remove
friends.remove("Charlie")  # Remove Charlie from the list

# Pop
popped_friend = friends.pop()  # Remove and return the last element
print(f"Removed friend: {popped_friend}")
print(friends)  # Print the updated list

# Count
count_of_bobs = friends.count("Bob")  # Count occurrences of Bob
print(f"Number of Bobs: {count_of_bobs}")

# Sort
friends.sort()  # Sort the list in ascending order
print(f"Sorted friends: {friends}")

# Reverse
friends.reverse()  # Reverse the order of the list
print(f"Reversed friends: {friends}")

