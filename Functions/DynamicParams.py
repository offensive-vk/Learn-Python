def dynamic_params_example(*args, **kwargs):
    """
    Function to demonstrate dynamic parameters in Python.
    
    Args:
        *args: Variable number of positional arguments.
        **kwargs: Variable number of keyword arguments.
    """
    print("Positional arguments:")
    for arg in args:
        print(arg)
        
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage of the function with different types of parameters
dynamic_params_example(1, 2, 3, name="Alice", age=30)
