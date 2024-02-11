# File Handling Functions Example

# Open a file for writing
with open('example.txt', 'w') as file:
    # Write content to the file
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")

# Open the same file for reading
with open('example.txt', 'r') as file:
    # Read content from the file
    content = file.read()
    print("Content of the file:")
    print(content)

# Open the same file for appending
with open('example.txt', 'a') as file:
    # Append new content to the file
    file.write("Appending new content!\n")

# Open the same file for reading and writing
with open('example.txt', 'r+') as file:
    # Read content from the file
    content = file.read()
    print("\nContent of the file before modification:")
    print(content)

    # Move the cursor to the beginning of the file
    file.seek(0)

    # Modify the content
    file.write("Modified content!\n")

    # Move the cursor to the beginning of the file
    file.seek(0)

    # Read the modified content
    modified_content = file.read()
    print("\nModified content of the file:")
    print(modified_content)

# Using tell() to get the current file pointer position
with open('example.txt', 'r') as file:
    file.seek(0)
    print("\nCurrent file pointer position:", file.tell())

# Using seek() to move the file pointer to a specific position
with open('example.txt', 'r') as file:
    file.seek(5)  # Move to the 6th character (0-based indexing)
    print("\nFile pointer moved to position:", file.tell())
    print("Content after moving file pointer:")
    print(file.read())
