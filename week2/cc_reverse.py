def reverse(str):

	# My try
	'''rev = ""
	for i in range(len(str), 0, -1):
		rev += str[i-1]
	return rev'''

	# String Slicing
	return str[::-1]
	

name = input("What is your name? ")
print("Your name reversed is:", reverse(name))