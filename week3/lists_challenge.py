import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:

	quit = input("Press enter to pick a card, or Q plus enter to quit: ")
	if quit =='Q':
		break

	select_card = random.choice(diamonds)			# Select a random card
	card_index = diamonds.index(select_card)		# Get index of the selected card 
	card = diamonds.pop(card_index)					# Remove the item (card) at that index
	hand.append(card)								# Add the card to hand

	# hand.append(diamonds.pop(diamonds.index(random.choice(diamonds))))

	print("Deck:", diamonds)
	print("Hand:", hand)

if not diamonds:
	print("There are no more cards to pick.")
