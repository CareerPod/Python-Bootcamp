# Lists are mutable (can be modified) and allow various operations:



# 1. Creating a List
my_list = [1, 2, 3, "apple", "banana"]

# 2. Accessing Elements
print("First element:", my_list[0])  # Indexing
print("Last element:", my_list[-1])  # Negative indexing

# 3. Slicing
print("First three elements:", my_list[:3])

# 4. Adding Elements
my_list.append("cherry")  # Adds an element to the end
print("After append:", my_list)

my_list.insert(2, "orange")  # Adds at a specific position
print("After insert:", my_list)

# 5. Removing Elements
my_list.remove("banana")  # Removes the first occurrence
print("After remove:", my_list)

popped_item = my_list.pop()  # Removes the last element
print("Popped item:", popped_item)
print("After pop:", my_list)

# 6. Length of List
print("Length of the list:", len(my_list))

# 7. Iterating over a List
for item in my_list:
    print("Item:", item)

# 8. Sorting a List
numbers = [5, 2, 9, 1, 3]
numbers.sort()  # Ascending sort
print("Sorted list:", numbers)

numbers.reverse()  # Reverses the list
print("Reversed list:", numbers)
