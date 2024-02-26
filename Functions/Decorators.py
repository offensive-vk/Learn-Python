def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function", func.__name__, "finished execution")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print("Result:", result)

# Decorator Example 1
def decorator_example_1(func):
    def wrapper(*args, **kwargs):
        print("Decorator Example 1 - Before function execution")
        result = func(*args, **kwargs)
        print("Decorator Example 1 - After function execution")
        return result
    return wrapper

@decorator_example_1
def function_1():
    print("Function 1 executed")

function_1()

# Decorator Example 2
def decorator_example_2(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{message} - Before function execution")
            result = func(*args, **kwargs)
            print(f"{message} - After function execution")
            return result
        return wrapper
    return decorator

@decorator_example_2("Decorator Example 2")
def function_2():
    print("Function 2 executed")

function_2()

"""
A decorator in Python is a design pattern that allows you to extend or modify the behavior of functions or methods without changing their actual code. It is a function that takes another function as an argument and returns a new function, usually adding some kind of functionality before or after the original function is called.
"""