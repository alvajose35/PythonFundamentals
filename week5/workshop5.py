import random

# User input
def guess_random_number(tries: int, start: int, stop:int):

	target = random.randint(start, stop)
	guess_list = []

	while tries > 0:

		print(f"\nYou have {tries} left.")
		guess = int(input(f"Guess a number between {start} and {stop}: "))

		# Bonus Task 1
		if guess < start or guess > stop:
			print("\nYour guess is outside the range of possible values...")
			continue

		# Bonus Task 3
		if guess in guess_list:
			print(f"\nYou already tried to guess {guess}")
			continue

		guess_list.append(guess)

		if guess == target:
			print("You guess the correct number!")
			return guess
		elif guess < target:
			print("Guess higher!")
		else:
			print("Guess lower!")

		tries -= 1
	
	print(f"You have failed to guess the number: {target}")

# Linear search
def guess_random_num_linear(tries: int, start: int, stop:int):

	target = random.randint(start, stop)
	print(f"The number for the program to guess is: {target}")

	for guess in range(tries):

		print("Number of tries left:", tries)
		print("The program is guessing...", guess)

		if guess == target:
			print("The program has guessed the correct number!")
			return guess
		
		tries -= 1
	
	print("The program has failed to guess the correct number.")

# Binary search
def guess_random_num_binary(tries: int, start: int, stop:int):

	target = random.randint(start, stop)
	print(f"The number for the program to guess is: {target}")

	while tries > 0:

		guess = (start + stop) // 2
		print("\nNumber of tries left:", tries)
		print("The program is guessing...", guess)

		if guess == target:
			print("Found it!", guess)
			break
		if guess > target:
			print("Guessing lower!")
			stop = guess - 1
		else:
			print("Guessing higher!")
			start = guess + 1

		tries -= 1
		if tries <= 0:
			print("\nThe program has failed to guess the correct number.")
			break

# Bonus Task 2
def bonus_task2():

	# Ask user for input values
	tries = int(input("Enter the amount of tries: "))
	start = int(input("Enter the lower bound: "))
	stop = int(input("Enter the upper bound: "))

	print("\nWhich method would you like to use?")
	print("1. User Input")
	print("2. Linear Search")
	print("3. Binary Search")

	use = int(input("\nEnter the number of the method you choose: "))

	if use == 1:
		guess_random_number(tries, start, stop)
	elif use == 2:
		guess_random_num_linear(tries, start, stop)
	elif use == 3:
		guess_random_num_binary(tries, start, stop)
	else:
		print("You have entered a an invalid option.")


	

# Driver Code for Task 1
guess_random_number(5, 0, 10)

# Driver Code for Task 2
'''guess_random_num_linear(5, 0, 10)'''

# Driver Code for Task 3
'''guess_random_num_binary(15, 0, 10000)'''

# Driver Code for Bonus 2
'''bonus_task2()'''