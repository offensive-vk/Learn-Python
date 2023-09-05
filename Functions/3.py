def get_names():
    names = []
    for i in range(3):
        name = input("Enter a name: ")
        names.append(name)
    return names

# Call the function to get the names and store them in a list
name_list = get_names()

# Display the list of names
print("List of names:", name_list)
