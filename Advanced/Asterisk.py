# Various use cases of (*) in Python :
# Function to demonstrate variable-length arguments (*args)
def print_args(*args):
    print("Variable-Length Arguments (*args):")
    for arg in args:
        print(arg)
    print()

# Function to demonstrate unpacking iterables
def unpacking_iterable():
    my_list = [1, 2, 3]
    print("Unpacking Iterables:")
    print(*my_list)
    print()

# Function to demonstrate extended unpacking
def extended_unpacking():
    my_list = [1, 2, 3, 4, 5]
    first, *rest = my_list
    print("Extended Unpacking:")
    print("First element:", first)
    print("Rest of the elements:", rest)
    print()

# Function to demonstrate keyword arguments (**kwargs)
def print_kwargs(**kwargs):
    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print()

# Test the functions
if __name__ == "__main__":
    print_args(1, 2, 3, 4, 5)
    unpacking_iterable()
    extended_unpacking()
    print_kwargs(name="Manish", age=20)
