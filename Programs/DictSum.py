# Write a python program to find the sum of dictionary values

def sum_dictionary_values(dictionary):
    total_sum = 0
    for value in dictionary.values():
        total_sum += value
    return total_sum

# Example usage
my_dictionary = {"a": 1, "b": 2, "c": 3}
sum_of_values = sum_dictionary_values(my_dictionary)
print("The sum of the dictionary values is:", sum_of_values)