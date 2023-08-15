
# Create a dictionary
student = {
    'name': 'Rupesh Don',
    'age': 20,
    'major': 'Computer Science',
    'gpa': 3.8,
    'isPass': True
}

# Access values in a dictionary
student_name = student['name']
student_age = student.get('age')

# Modify values in a dictionary
student['gpa'] = 3.9

# Add a new key-value pair
student['email'] = 'john.doe@example.com'

# Remove a key-value pair
removed_major = student.pop('major')

# Check if a key exists in the dictionary
has_major = 'major' in student

# Get a list of keys and values
keys = student.keys()
values = student.values()

# Get a list of key-value pairs
items = student.items()

# Create a copy of the dictionary
student_copy = student.copy()

# Clear all items from the dictionary
student.clear()

# Print the results
print("Original dictionary:", student_copy)
print("Student name:", student_name)
print("Student age:", student_age)
print("Updated GPA:", student['gpa'])
print("Removed major:", removed_major)
print("Has 'major' key:", has_major)
print("Keys:", keys)
print("Values:", values)
print("Items:", items)
