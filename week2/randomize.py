import random

pips = random.randint(1, 6)
print("You rolled the die... it lands with" , pips, "pips showing.")

prizes = ["a car", "$1000", "a pony", "$500000"]
prize_won = random.choice(prizes)
print("You turn the wheel of furtune... It lands on a prize of", prize_won + "!!")

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
random.shuffle(cards)
print("The cards are now in this order: ")
print(cards)
