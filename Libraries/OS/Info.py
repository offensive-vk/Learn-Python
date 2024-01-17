import os

def display_information():
    # Get and display the current working directory
    current_directory = os.getcwd()
    print(f"Current Working Directory: {current_directory}")

    # Get and display information about the user environment variables
    print("\nEnvironment Variables:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")

    # Check the existence of a specific file
    file_path = '/path/to/your/file.txt'
    if os.path.exists(file_path):
        print(f"\nFile '{file_path}' exists.")
    else:
        print(f"\nFile '{file_path}' does not exist.")

if __name__ == "__main__":
    display_information()
