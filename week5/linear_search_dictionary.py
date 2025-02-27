def linear_search_dictionary(the_dict, target):

	for x in the_dict:
		if the_dict[x] == target:
			print(f"Found at key {x}")
			return x
	
	print("Target is not in the dictionary")
	return None

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)