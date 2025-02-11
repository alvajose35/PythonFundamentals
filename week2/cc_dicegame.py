import random

high_score = 0

# Roll dice function
def roll_dice():
	return random.randint(1, 6)

# Main game
def dice_game():

	# Use global variable
	global high_score

	while True:

		# Initial state
		print("Current High Score:", high_score)
		print("1) Roll Dice")
		print("2) Leave Game")
		choice = input("Enter your choice: ")

		if choice == "1":

			# Roll dice and get total
			dice1 = roll_dice()
			dice2 = roll_dice()
			total = dice1 + dice2

			print("\nYou rolled a...", dice1)
			print("You rolled a...", dice2)
			print("\nYou have rolled a total of:", total, "\n")

			if total > high_score:
				high_score = total
				print("New high score!\n")
						
		elif choice == "2":
			print("Exiting game...")
			break
			# exit()

		else:
			print("Invalid Input\n")

dice_game()
