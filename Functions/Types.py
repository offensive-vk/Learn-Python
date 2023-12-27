"""
In Python, you can specify the data type of a function parameter using type hints.
Type hints are annotations added to the function parameters or the function's return value to indicate the expected data type.
However, it's important to note that Python is a dynamically-typed language, and type hints are not enforced at runtime.
They serve as documentation and can be used by tools like linters or static analyzers to catch potential type-related errors.
"""

from typing import List, Dict

def sayHello(name: str) -> str:
    return f"Hello ${name} , Nice to meet you."
def sort_descending(numbers: List[float]) -> List[float]:
    return sorted(numbers, reverse=True)
def sort_dict(input_dict: Dict[str, List[float]]) -> Dict[str, List[float]]:
    sorted_dict = {key: sorted(values, reverse=True) for key, values in input_dict.items()}
    return sorted_dict


# Example usage:
input_dictionary = {'a': [3.5, 1.2, 7.8, 2.0, 5.4], 'b': [9.1, 4.0, 6.3, 2.7]}
sorted_dictionary = sort_dict(input_dictionary)
print(sorted_dictionary)


# Example usage:
numbers_list = [3.5, 1.2, 7.8, 2.0, 5.4]
print(sort_descending(numbers_list))