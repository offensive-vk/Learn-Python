# Lists in Python

# Create a list
fruits = ['apple', 'banana', 'cherry', 'date', 'strawberry']
print("Old List: ", fruits)
print("\n===================")

# Get the length of the list
print(len(fruits))

# Append an item to the end of the list
fruits.append('pineapple')

# Insert an item at a specific position
fruits.insert(2, 'grape')

# Remove an item from the list
fruits.remove('cherry')

# Remove an item at a specific index
removed_item = fruits.pop(3)

# Get the index of an item
index_banana = fruits.index('banana')


# Count the occurrences of an item
fruits.append("apple")
count_apple = fruits.count('apple')


# Sort the list in ascending order
fruits.sort()


# Reverse the list
fruits.reverse()

# Create a copy of the list
fruits_copy = fruits.copy()


# Extend the list with another list
more_fruits = ['kiwi', 'lemon', 'mango']
fruits.extend(more_fruits)
print(fruits)

# Clear all items from the list
fruits.clear()
print(fruits)

# Print the results
print("Original list:", fruits_copy)
print("Appended list:", fruits)
print("Removed item:", removed_item)
print("Index of 'banana':", index_banana)
print("Count of 'apple':", count_apple)
