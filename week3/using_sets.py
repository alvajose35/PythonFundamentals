numbers_set1 = {1, 2, 3, 4}
print(numbers_set1)

# Duplicate values removed
numbers_set2 = {1, 2, 3, 4, 4}
print(numbers_set2)

# Cannot use mutable data types
# numbers_set3 = {1, 2, 3, 4, [5, 6]}

# Tuples are immutable, OK to use!
numbers_set3 = {1, 2, 3, 4, (5, 6)}	
print(numbers_set3)

# Access set values
words_set = {"Alpha", "Bravo", "Charlie"}


abcd = ""
for word in words_set:
    abcd += word
print(abcd)		# It changes each time the program runs since sets are unordered

# Check if value exists in a set
if "Alpha" in words_set:
	print("Alpha is in set")
else:
	print("Alpha not in set")

# Modify set values
words_set.add("Delta")
print(words_set)
words_set.discard("Bravo")
print(words_set)
