def greet(name="User", greeting="Hello"):
    return f"{greeting}, {name}!"

# Example usage of the function with default parameter
print(greet("Ali"))  # Output: Hello, Alice!

# Example usage of the function with custom parameter
print(greet("John", "Hey"))  # Output: Hey, Bob!