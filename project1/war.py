import random

# Functions
def cardValue(card):

	if card[0] == '2' or card[0] == '3' or card[0] == '4' or card[0] == '5' or card[0] == '6' or card[0] == '7' or card[0] == '8' or card[0] == '9':
		return int(card[0])
	elif card[0] == 'T':
		return 10
	elif card[0] == 'J':
		return 11
	elif card[0] == 'Q':
		return 12
	elif card[0] == 'K':
		return 13
	elif card[0] == 'A':
		return 14
	elif card[0] == 'X':
		return 15
	else:
		return "ERROR"

def reshuffle(deck, pile):

	deck = deck + pile
	random.shuffle(deck)
	pile = []

	return deck, pile

def checkGameOver(num_of_cards, all_decks):

	# Check Computer
	if len(all_decks[0]) < num_of_cards:     # compDeck < n

		if len(all_decks[0]) + len(all_decks[1]) < num_of_cards:     # (compDeck & compPile) < n aka Comp LOST
			
			print("COMP: Not enough cards in deck and pile combined.")
			print("Needs: " + str(num_of_cards) + "   Has: " + str(len(all_decks[0]) + len(all_decks[1])) + " total cards.")
			print("\nGAME OVER. User wins!! (Computer lost)")
			return True, all_decks
		
		elif len(all_decks[0]) + len(all_decks[1]) >= num_of_cards:	    # reshuffle comp

			print("\nComputer reshuffle required...\n")
			all_decks[0], all_decks[1] = reshuffle(all_decks[0], all_decks[1])

			# Check to see if user also needs reshuffling
			x, all_decks = checkGameOver(num_of_cards, all_decks)

			return False, all_decks
	
	# Check User
	if len(all_decks[2]) < num_of_cards:     # userDeck < n
		if len(all_decks[2]) + len(all_decks[3]) < num_of_cards:     # (userDeck & userPile) < n aka User LOST

			print("USER: Not enough cards in deck and pile combined.")
			print("Needs: " + str(num_of_cards) + "   Has: " + str(len(all_decks[2]) + len(all_decks[3])) + " total cards.")
			print("\nGAME OVER. Computer wins!! (User lost)")
			return True, all_decks
		
		elif len(all_decks[2]) + len(all_decks[3]) >= num_of_cards:     # reshuffle user

			print("\nUser reshuffle required...\n")
			all_decks[2], all_decks[3] = reshuffle(all_decks[2], all_decks[3])
			return False, all_decks
	
	# Game Continues
	return False, all_decks


	# Assign global variables
	'''global comp_deck, user_deck, comp_pile, user_pile
	
	if (len(comp_deck) + len(comp_pile)) == 0:
		print("Game Over. User wins!! (Computer lost)")
		return True
	
	elif len(user_deck) + len(user_pile) == 0:
		print("Game Over. Computer wins!! (User lost)")
		return True
	
	else:
		return False'''

def war(k, j):

	global comp_deck, user_deck, comp_pile, user_pile

	# Check game status
	all_decks = [comp_deck, comp_pile, user_deck, user_pile]
	gameOver, all_decks = checkGameOver(k + 4, all_decks)
	if gameOver:
		exit()
		return
	comp_deck = all_decks[0]
	comp_pile = all_decks[1]
	user_deck = all_decks[2]
	user_pile = all_decks[3]

	# Print game screen
	print("\n----------WAR----------")
	
	for i in range(j):
		if i == 0:
			print("COMP: ", end='')
			print(comp_deck[-1], end='')
		print(" [X][X][X] ", end='')
		print(comp_deck[-(4*(i+1)+1)], end ='')
	print()

	for i in range(j):
		if i == 0:
			print("USER: ", end='')
			print(user_deck[-1], end='')
		print(" [X][X][X] ", end='')
		print(user_deck[-(4*(i+1)+1)], end='')
	print()

	# Evaluate winner (card values)
	if cardValue(comp_deck[-k-4]) > cardValue(user_deck[-k-4]):
		print("\nComputer Wins War!")
		for i in range(k+4):
			comp_pile.append(comp_deck.pop())
			comp_pile.append(user_deck.pop())

	elif cardValue(comp_deck[-k-4]) < cardValue(user_deck[-k-4]):
		print("\nUser Wins War!")
		for i in range(k+4):
			user_pile.append(comp_deck.pop())
			user_pile.append(user_deck.pop())
	
	else:
		print("\nSame card again!! War #", j + 1)
		input()
		war(k + 4, j + 1)


# Declare variables & Create a deck of cards
deck = [
	"2♠️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "T♠️", "J♠️", "Q♠️", "K♠️", "A♠️", 
	"2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "T♥️", "J♥️", "Q♥️", "K♥️", "A♥️",
	"2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "T♦️", "J♦️", "Q♦️", "K♦️", "A♦️",
	"2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️", "8♣️", "9♣️", "T♣️", "J♣️", "Q♣️", "K♣️", "A♣️",
	"XB", "XR"
]

comp_pile = []
user_pile = []

# Shuffle cards and split them
random.shuffle(deck)

comp_deck = deck[:27]
user_deck = deck[27:]

# Un-comment to test reshuffle
'''tempDeckComp = ["7♠️", "T♠️", "4♠️", "5♠️", "5♠️"]
tempDeckUser = ["4♦️", "9♦️", "Q♦️", "K♦️", "A♦️"]
comp_deck = tempDeckComp
user_deck = tempDeckUser'''

# print(comp_deck)
# print(user_deck)

while True:

	# Check game status
	all_decks = [comp_deck, comp_pile, user_deck, user_pile]
	gameOver, all_decks = checkGameOver(1, all_decks)

	if gameOver:
		break
	comp_deck = all_decks[0]
	comp_pile = all_decks[1]
	user_deck = all_decks[2]
	user_pile = all_decks[3]
	
	# Assig value to cards
	comp_card_v = cardValue(comp_deck[-1])
	user_card_v	= cardValue(user_deck[-1])

	# PRINT SCREEN
	print("\n----------GAME----------")

	# print(comp_deck[-1], comp_card_v)
	# print(user_deck[-1], user_card_v)

	print("COMP: [" + str(len(comp_deck) - 1) + "]  " + comp_deck[-1])
	print("USER: [" + str(len(user_deck) - 1) + "]  " + user_deck[-1])

	if comp_card_v > user_card_v:
		print("\nComputer Wins Hand!\n")
	elif comp_card_v < user_card_v:
		print("\nPlayer Wins Hand!\n")
	else:
		print("\nSame Card!!! War time!!!\n")
		input()
		war(1, 1)
		# print("\nBACK FROM FUNCT\n")

	print(str(len(comp_pile)) + " - Computer's Pile:",  comp_pile)
	print(str(len(user_pile)) + " - User's Pile:", user_pile)

	if comp_card_v > user_card_v:
		comp_pile.append(comp_deck.pop())
		comp_pile.append(user_deck.pop())
	elif comp_card_v < user_card_v:
		user_pile.append(comp_deck.pop())
		user_pile.append(user_deck.pop())

	input()

print("Thanks for playing")