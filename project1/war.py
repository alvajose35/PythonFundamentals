import random

# Function: return card value
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

# Declare variables & Create a deck of cards
'''deck = [
	"2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "QS", "KS", "AS",
	"2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH", "AH",
	"2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD", "AD",
	"2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC", "AC",
	"XB", "XR"
]'''

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

# Shuffle cards and plit two piles
random.shuffle(deck)

comp_deck = deck[:27]
user_deck = deck[27:]

print(comp_deck)
print(user_deck)

# print("----")
# print(comp_deck[-1])
# print(user_deck[-1])
# print("----")

'''comp_card = comp_deck.pop()
user_card = user_deck.pop()

print(comp_card)
print(user_card)'''

# print(comp_deck)
# print(user_deck)

'''comp_card_v = cardValue(comp_card)
user_card_v	= cardValue(user_card)'''


while dealHand:
	
	comp_card_v = cardValue(comp_deck[-1])
	user_card_v	= cardValue(user_deck[-1])

	print(comp_deck[-1], comp_card_v)
	print(user_deck[-1], user_card_v)

	# print(comp_card_v)
	# print(user_card_v)


	# PRINT SCREEN
	print("---------------------------------------")

	print("COMP: [" + str(len(comp_deck) - 1) + "]  " + comp_deck[-1])     # print("COMP: [" + str(len(comp_deck)) + "]  " + comp_card)
	print("USER: [" + str(len(user_deck) - 1) + "]  " + user_deck[-1])     # print("USER: [" + str(len(user_deck)) + "]  " + user_card)

	if comp_card_v > user_card_v:
		print("\nComputer Wins!\n")
	elif comp_card_v < user_card_v:
		print("\nPlayer Wins!\n")
	else:
		print("\nWAR\n")


	print("Computer's Pile:", comp_pile)
	print("User's Pile:", user_pile)

	'''if comp_card_v > user_card_v:
		comp_pile.append(comp_card)
		comp_pile.append(user_card)
	elif comp_card_v < user_card_v:
		user_pile.append(comp_card)
		user_pile.append(user_card)
	else:
		print("WAR GAME")'''

	if comp_card_v > user_card_v:
		comp_pile.append(comp_deck.pop())
		comp_pile.append(user_deck.pop())
	elif comp_card_v < user_card_v:
		user_pile.append(comp_deck.pop())
		user_pile.append(user_deck.pop())
	else:
		print("WAR GAME")

	input()

print("Computer's Pile:", comp_pile)
print("User's Pile:", user_pile)
print(comp_deck)
print(user_deck)


