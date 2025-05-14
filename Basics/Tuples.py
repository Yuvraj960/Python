"""

Tuples are immutable sequences, typically used to store collections of heterogeneous data.
Tuples are similar to lists, but they cannot be changed after creation.
Tuples are defined by enclosing the elements in parentheses ().


"""

tuple1 = (1, 2, 3, "hello", 4.5, True)

print(type(tuple1))  # <class 'tuple'>
print(tuple1[0])  # First element

print(tuple1[1])  # Second element
print(tuple1[-1])  # Last element

print(tuple1[1:4])  # Slice from index 1 to 3 (4 is not included)

print(tuple1[:3])  # Slice from start to index 2 (3 is not included)

# Tuple Methods

# Count
count_of_ones = tuple1.count(1)
print(f"Number of ones: {count_of_ones}")

# Index
index_of_hello = tuple1.index("hello")
print(f"Index of 'hello': {index_of_hello}")

# Tuple Unpacking
a, b, c, d, e, f = tuple1
print(f"Unpacked values: {a}, {b}, {c}, {d}, {e}, {f}")

# Tuple Concatenation
tuple2 = (6, 7, 8)
concatenated_tuple = tuple1 + tuple2
print(f"Concatenated tuple: {concatenated_tuple}")

# Tuple Repetition
repeated_tuple = tuple1 * 2
print(f"Repeated tuple: {repeated_tuple}")

# Tuple Membership
is_five_in_tuple = 5 in tuple1
print(f"Is 5 in tuple: {is_five_in_tuple}") # False

# Tuple Length
tuple_length = len(tuple1)
print(f"Length of tuple: {tuple_length}")

# Min and Max
min_value = min(tuple1)
print(f"Minimum value in tuple: {min_value}")
max_value = max(tuple1)
print(f"Maximum value in tuple: {max_value}")