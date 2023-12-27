from typing import List

def sort_descending(numbers: List[float]) -> List[float]:
    """
    Sorts a list of numbers in descending order.

    Parameters:
    - numbers (List[float]): List of numbers to be sorted.

    Returns:
    - List[float]: Sorted list in descending order.
    """
    return sorted(numbers, reverse=True)

# Example usage:
numbers_list = [3.5, 1.2, 7.8, 2.0, 5.4]
sorted_numbers = sort_descending(numbers_list)
print(sorted_numbers)
