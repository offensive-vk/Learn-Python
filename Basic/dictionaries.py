# Create a dictionary
student = {
    'name': 'Rupesh Don',
    'age': 20,
    'major': 'Computer Science',
    'gpa': 2.8,
    'isPass': True
}
print("Old Dictionary: ",student)

# Access values in a dictionary
student_name = student['name']
student_age = student.get('age')

# Modify values in a dictionary
student['gpa'] = 3.9
student['major'] = "Commerce"
print(student)

# Add a new key-value pair
student['favorites'] = ["anime", "manga", "18+"]
print(student)

# Remove a key-value pair
removed_major = student.pop('major')
print(removed_major)
print(student)

# Check if a key exists in the dictionary
has_major = 'manish' in student
print(has_major)

# Get a list of keys and values
keys = student.keys()
values = student.values()
print(keys)
print(values)

# Get a list of key-value pairs
items = student.items()
print(items)

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