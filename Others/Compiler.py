# Write a program that compiles all the present file with extensions - cpp, cxx, c++ and save the exe file to diff folder.
import os

def main():
    # Get the current working directory
    current_directory = os.getcwd()

    # List all files in the current working directory
    files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]

    # Print the list of files
    print(f"Starting compilation in current working directory : {current_directory}\n")
    for file in files:
        if file.endswith('.cpp') or file.endswith('.cxx') or file.endswith('.c++'):
            command = f"g++ {file} -o output/{file.split('.')[0]}"
            os.system(command)
            print("Finished Compilation.")

if __name__ == '__main__':
    main()
