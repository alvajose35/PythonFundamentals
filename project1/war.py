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

def checkGameOver():

	# Assign global variables
	global comp_deck, user_deck, comp_pile, user_pile
	
	if (len(comp_deck) + len(comp_pile)) == 0:
		print("Game Over. User wins!! (Computer lost)")
		return True
	
	elif len(user_deck) + len(user_pile) == 0:
		print("Game Over. Computer wins!! (User lost)")
		return True
	
	else:
		return False

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

dealHand = True

tempDeckComp = ["2♠️", "3♠️", "4♠️", "5♠️", "6♠️"]
tempDeckUser = ["T♦️", "J♦️", "Q♦️", "K♦️", "A♦️"]

# Shuffle cards and plit two piles
random.shuffle(deck)

# comp_deck = deck[:27]
# user_deck = deck[27:]

comp_deck = tempDeckComp
user_deck = tempDeckUser


print(comp_deck)
print(user_deck)

while dealHand:

	# Check status
	gameOver = checkGameOver()
	if gameOver:
		break
	
	comp_card_v = cardValue(comp_deck[-1])
	user_card_v	= cardValue(user_deck[-1])

	# PRINT SCREEN
	print("---------------------------------------")

	print(comp_deck[-1], comp_card_v)
	print(user_deck[-1], user_card_v)

	print("COMP: [" + str(len(comp_deck) - 1) + "]  " + comp_deck[-1])
	print("USER: [" + str(len(user_deck) - 1) + "]  " + user_deck[-1])

	if comp_card_v > user_card_v:
		print("\nComputer Wins!\n")
	elif comp_card_v < user_card_v:
		print("\nPlayer Wins!\n")
	else:
		print("\nWAR\n")


	print("Computer's Pile:", comp_pile)
	print("User's Pile:", user_pile)

	if comp_card_v > user_card_v:
		comp_pile.append(comp_deck.pop())
		comp_pile.append(user_deck.pop())
	elif comp_card_v < user_card_v:
		user_pile.append(comp_deck.pop())
		user_pile.append(user_deck.pop())
	else:
		print("WAR GAME")

	input()

print("SHUTING OFF")