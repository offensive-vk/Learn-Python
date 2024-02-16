from typing import Union

def print_value(value: Union[int, float, str]):
    """
    Function to print the value provided, which can be an integer, float, or string.
    
    Args:
        value (Union[int, float, str]): The value to be printed.
    """
    print(value)

# Example usage of the function with different types of parameters
print_value(10)         # Output: 10
print_value(3.14)       # Output: 3.14
print_value("Hello")    # Output: Hello