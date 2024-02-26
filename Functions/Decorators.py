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
