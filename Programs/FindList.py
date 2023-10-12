def find(lst):
    smallest = min(lst)
    largest = max(lst)
    return smallest, largest

numbers = [5, 2, 9, 1, 7]
smallest_num, largest_num = find(numbers)
print("Smallest number:", smallest_num)
print("Largest number:", largest_num)


