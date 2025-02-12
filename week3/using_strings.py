my_string = "alpha"
print(my_string)

# Create a multiline string
multiline_string = """bravo
charlie"""
print(multiline_string)

# Retrieve single characters by index
print(my_string[0])
print(my_string[3])

# Slicing substrings
print(my_string[0:3])
print(my_string[:2])
print(my_string[2:])
print(my_string)

# Testing string immutability
# my_string[0] = "b"

# Iterate string using for ... in
for char in my_string:
    print(char)

# Check if substring exists in a string
print("pha" in my_string)
print("z" not in my_string)
