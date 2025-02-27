import random
import math

def interpolation_search(the_list, target):
	
	lower_bound = 0
	upper_bound = len(the_list) - 1

	while target >= the_list[lower_bound] and target <= the_list[upper_bound] and lower_bound <= upper_bound:

		probe_fl = lower_bound + (upper_bound - lower_bound) * (target - the_list[lower_bound]) // (the_list[upper_bound] - the_list[lower_bound])
		probe = int(probe_fl)

		print(f"Probe: {probe}     ||Value at probe: {the_list[probe]}")
		

		if the_list[probe] == target:
			return probe
		elif the_list[probe] < target:
			lower_bound = probe + 1
		else:
			upper_bound = probe - 1

	return -1

# ======================================================

'''my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(interpolation_search(my_list, 10))
print(interpolation_search(my_list, 4))
print(interpolation_search(my_list, 33))'''

# ======================================================

def generate_uniform_list(size, min_val, max_val):
    """
    Generates a list of uniformly distributed random numbers.

    Args:
        size: The number of random numbers to generate.
        min_val: The minimum value of the range.
        max_val: The maximum value of the range.

    Returns:
        A list of uniformly distributed random numbers.
    """
    random_list = []
    for _ in range(size):
        random_list.append(int(math.floor(random.uniform(min_val, max_val))))
    return random_list

# ======================================================

my_list = generate_uniform_list(1000, 0, 1000)
my_list.sort()

print(my_list)

match = -1

while match == -1:
	val = random.randint(0,1000)
	print(f"Value: {val}")
	print(interpolation_search(my_list, val))
	match = interpolation_search(my_list, val)