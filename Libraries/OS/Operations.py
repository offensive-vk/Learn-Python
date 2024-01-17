import os

def perform_operations():
    # Create a new directory
    new_directory = '/path/to/your/new_directory'
    os.makedirs(new_directory, exist_ok=True)
    print(f"Created a new directory: {new_directory}")

