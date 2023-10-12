def remove_duplicates(string):
    # Convert the string to a set to remove duplicates
    unique_chars = set(string)
    
    # Join the unique characters back into a string
    result = ''.join(unique_chars)
    
    return result


s = "Hello , Hello"
result = remove_duplicates(s)
print(result)

