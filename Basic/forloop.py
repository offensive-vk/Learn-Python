# List
print("For Loop with List:")
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# String
print("\nFor Loop with String:")
my_string = "Hello"
for char in my_string:
    print(char)

# Tuple
print("\nFor Loop with Tuple:")
my_tuple = (6, 7, 8, 9, 10)
for item in my_tuple:
    print(item)

# Range
print("\nFor Loop with Range:")
for num in range(1, 6):
    print(num)

# Dictionary
print("\nFor Loop with Dictionary:")
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
for key, value in my_dict.items():
    print(key, ":", value)

# Set
print("\nFor Loop with Set:")
my_set = {11, 12, 13, 14, 15}
for item in my_set:
    print(item)

# Bytes (Python 3)
print("\nFor Loop with Bytes:")
my_bytes = b'byte string'
for byte in my_bytes:
    print(byte)
