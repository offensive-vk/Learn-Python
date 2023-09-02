# Create a tuple
colors = ('red', 'green', 'blue', 'yellow', 'orange')

# Access elements of a tuple
first_color = colors[0]
second_color = colors[1]

# Find the index of an item
index_blue = colors.index('blue')

# Count the occurrences of an item
count_green = colors.count('green')

# Convert a tuple to a list
colors_list = list(colors)

# Convert a list back to a tuple
colors_tuple = tuple(colors_list)

# Print the results
print("Original tuple:", colors)
print("First color:", first_color)
print("Second color:", second_color)
print("Index of 'blue':", index_blue)
print("Count of 'green':", count_green)
print("Converted to list:", colors_list)
print("Converted back to tuple:", colors_tuple)
