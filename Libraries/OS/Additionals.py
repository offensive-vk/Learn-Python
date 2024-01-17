import os
import time

def additional_os_operations():
    # Get the current process ID
    process_id = os.getpid()
    print(f"Current Process ID: {process_id}")

    # Get the login name
    login_name = os.getlogin()
    print(f"Login Name: {login_name}")

    # Create a temporary file
    temp_file_path = 'temp_file.txt'
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write("This is a temporary file.")

    # Get file information
    file_info = os.stat(temp_file_path)
    print("\nFile Information:")
    print(f"Size: {file_info.st_size} bytes")
    print(f"Last Access Time: {time.ctime(file_info.st_atime)}")
    print(f"Last Modification Time: {time.ctime(file_info.st_mtime)}")


