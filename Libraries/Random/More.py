import random

# Generate a random floating-point number
random_float = random.random()
print("Random float between 0 and 1:", random_float)

# Generate a random integer within a specific range
random_int = random.randint(1, 100)
print("Random integer between 1 and 100:", random_int)

# Select a random element from a list
my_list = ['apple', 'banana', 'cherry', 'date']
random_element = random.choice(my_list)
print("Random element from the list:", random_element)

# Shuffle a list in place
random.shuffle(my_list)
print("Shuffled list:", my_list)

# Get a random sample without replacement
random_sample = random.sample(my_list, 2)
print("Random sample of 2 elements without replacement:", random_sample)

# Get a random sample with replacement (allowing duplicates)
random_sample_with_replacement = [random.choice(my_list) for _ in range(3)]
print("Random sample of 3 elements with replacement:", random_sample_with_replacement)

# Generate a random integer from a normal distribution with specified mean and standard deviation
mean = 0
std_dev = 1
random_normal = random.gauss(mean, std_dev)
print("Random number from normal distribution (mean={}, std_dev={}): {:.2f}".format(mean, std_dev, random_normal))

# Generate a random integer from a triangular distribution with specified lower, mode, and upper values
lower = 1
mode = 5
upper = 10
random_triangular = random.triangular(lower, mode, upper)
print("Random number from triangular distribution (lower={}, mode={}, upper={}): {:.2f}".format(lower, mode, upper, random_triangular))
