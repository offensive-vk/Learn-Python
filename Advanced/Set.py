def demonstrate_set_functions():
    # Creating two sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}

    # Displaying the original sets
    print("Set 1:", set1)
    print("Set 2:", set2)

    # Union of sets
    union_set = set1.union(set2)
    print("Union of sets:", union_set)

    # Intersection of sets
    intersection_set = set1.intersection(set2)
    print("Intersection of sets:", intersection_set)

    # Difference between sets
    difference_set = set1.difference(set2)
    print("Difference between sets (set1 - set2):", difference_set)

    # Check if one set is a subset of another
    is_subset = set1.issubset(set2)
    print("Is set1 a subset of set2?", is_subset)

def demonstrate_all_function():
    # Example using the all() function
    numbers = [2, 4, 6, 8, 10]

    # Check if all numbers are even
    all_even = all(num % 2 == 0 for num in numbers)

    print("Are all numbers even?", all_even)

# Call the set functions demonstration
demonstrate_set_functions()

# Call the all function demonstration
demonstrate_all_function()
