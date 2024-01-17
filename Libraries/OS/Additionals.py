import os
import time

def additional_os_operations():
    # Get the current process ID
    process_id = os.getpid()
    print(f"Current Process ID: {process_id}")

    # Get the login name
    login_name = os.getlogin()
    print(f"Login Name: {login_name}")

