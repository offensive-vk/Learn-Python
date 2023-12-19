# Writing to a file
def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Reading from a file
def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content read from {file_path}:\n{content}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading from file: {e}")

# Example usage
file_path = 'example.txt'
write_content = 'Hello, this is a sample text.'
write_to_file(file_path, write_content)

read_from_file(file_path)