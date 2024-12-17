# 1. Creating a Tuple
my_tuple = (1, 2, 3, "apple", "banana")

# 2. Accessing Elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# 3. Slicing
print("First three elements:", my_tuple[:3])

# 4. Length of Tuple
print("Length of the tuple:", len(my_tuple))

# 5. Iterating over a Tuple
for item in my_tuple:
    print("Item:", item)

# 6. Count and Index
another_tuple = (1, 2, 3, 2, 4, 2)
print("Count of 2:", another_tuple.count(2))  # Count occurrences of an element
print("Index of 4:", another_tuple.index(4))  # Find position of an element
