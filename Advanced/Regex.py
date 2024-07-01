import re

def test_regex(pattern, test_strings):
    """
    Test the given regex pattern against a list of test strings.

    Args:
    pattern (str): The regex pattern to test.
    test_strings (list of str): The strings to test against the pattern.

    Returns:
    None
    """
    regex = re.compile(pattern)
    
    for string in test_strings:
        match = regex.fullmatch(string)
        if match:
            print(f"'{string}' matches the pattern.")
        else:
            print(f"'{string}' does not match the pattern.")

# Define some regex patterns to test
patterns = [
    r'^[a-zA-Z_][\w\[\], ().\"\']*(\.[a-zA-Z_][\w\[\], ]*)*$',  # The pattern we explained earlier
    r'^\d{3}-\d{2}-\d{4}$',  # Social Security number pattern (e.g., 123-45-6789)
    r'^[\w\.-]+@[\w\.-]+\.\w+$',  # Simple email pattern
    r'^(https?|ftp)://[^\s/$.?#].[^\s]*$',  # URL pattern
]

# Define some test strings for each pattern
test_strings = [
    # Test strings for the first pattern
    ['a', 'abc', 'a[1], b(2).c', 'a_b.c_d', 'a.b.c', 'var_name.method_name', '1abc', '!abc', 'a..b'],
    
    # Test strings for the second pattern
    ['123-45-6789', '987-65-4321', '123-456-789', '12-345-6789', '123456789'],
    
    # Test strings for the third pattern
    ['test@example.com', 'user.name@domain.co', 'user@domaincom', 'user@domain.', '@domain.com'],
    
    # Test strings for the fourth pattern
    ['http://example.com', 'https://example.com', 'ftp://example.com', 'htp://example.com', '://example.com'],
]

# Loop through each pattern and test strings
for i, pattern in enumerate(patterns):
    print(f"\nTesting pattern: {pattern}")
    test_regex(pattern, test_strings[i])
