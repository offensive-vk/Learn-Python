def demonstrate_tuples():
    # 1. Creating and accessing tuples
    print("1. Creating and accessing tuples:")
    my_tuple = (1, 2, 3, 'a', 'b', 'c')
    print("Tuple:", my_tuple)
    print("First element:", my_tuple[0])
    print("Last element:", my_tuple[-1])
    print("Slice:", my_tuple[1:4])

    # 2. Immutability of tuples
    print("\n2. Immutability of tuples:")
    try:
        my_tuple[0] = 100
    except TypeError as e:
        print("Error:", e)

    # 3. Tuples as return values from functions
    print("\n3. Tuples as return values from functions:")
    def min_max(numbers):
        return min(numbers), max(numbers)

    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = min_max(numbers)
    print("Numbers:", numbers)
    print("Min and Max:", result)

    # 4. Unpacking tuples
    print("\n4. Unpacking tuples:")
    min_val, max_val = result
    print("Min value:", min_val)
    print("Max value:", max_val)

    # 5. Tuples as keys in dictionaries
    print("\n5. Tuples as keys in dictionaries:")
    locations = {
        ('New York', 'NY'): 'Empire State Building',
        ('San Francisco', 'CA'): 'Golden Gate Bridge',
        ('Los Angeles', 'CA'): 'Hollywood Sign'
    }
    print("Locations dictionary:", locations)
    location = ('San Francisco', 'CA')
    print(f"Famous place in {location}:", locations.get(location, 'Unknown'))

    # 6. Nested tuples
    print("\n6. Nested tuples:")
    nested_tuple = ((1, 2), (3, 4), (5, 6))
    print("Nested tuple:", nested_tuple)
    for sub_tuple in nested_tuple:
        print("Sub-tuple:", sub_tuple)

    # 7. Tuple comprehension equivalent (not directly possible with tuples, but shown using generator expressions)
    print("\n7. Tuple comprehension equivalent using generator expressions:")
    squared_numbers = tuple(x * x for x in range(10))
    print("Squared numbers:", squared_numbers)

if __name__ == "__main__":
    demonstrate_tuples()
