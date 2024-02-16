from typing import Optional

def find_element(lst: Optional[list], target: int) -> Optional[int]:
    """
    Function to find an element in a list.

    Args:
        lst (Optional[list]): The list to search in.
        target (int): The element to find.

    Returns:
        Optional[int]: The index of the target element if found, else None.
    """
    if lst is not None:
        for i, num in enumerate(lst):
            if num == target:
                return i
    return None

# Example usage of the function
result1 = find_element([1, 2, 3, 4, 5], 3)
print(result1)  # Output: 2 (index of the element 3 in the list)

result2 = find_element(None, 5)
print(result2)  # Output: None (since the list is None)


def get_value(data: Optional[dict], key: str) -> Optional[str]:
    """
    Function to get a value from a dictionary.

    Args:
        data (Optional[dict]): The dictionary to get value from.
        key (str): The key to lookup.

    Returns:
        Optional[str]: The value corresponding to the key if found, else None.
    """
    if data is not None:
        return data.get(key)
    return None

# Example usage of the function
data = {"name": "John", "age": 30}
value1 = get_value(data, "name")
print(value1)  # Output: Alice

value2 = get_value(None, "age")
print(value2)  # Output: None (since the dictionary is None)