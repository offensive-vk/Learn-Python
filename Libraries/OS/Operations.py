import os

def perform_operations():
    # Create a new directory
    new_directory = '/path/to/your/new_directory'
    os.makedirs(new_directory, exist_ok=True)
    print(f"Created a new directory: {new_directory}")

    # Change the current working directory
    os.chdir(new_directory)
    print(f"Changed the current working directory to: {os.getcwd()}")

    # Create a new file in the current directory
    new_file_path = 'new_file.txt'
    with open(new_file_path, 'w') as new_file:
        new_file.write("Hello, this is a new file.")

    print(f"Created a new file: {new_file_path}")

    # Rename the file
    renamed_file_path = 'renamed_file.txt'
    os.rename(new_file_path, renamed_file_path)
    print(f"Renamed the file to: {renamed_file_path}")


