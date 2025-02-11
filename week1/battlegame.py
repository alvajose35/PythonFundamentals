
# Declare characters names 
wizard = "Wizard"
elf = "Elf"
human = "Human"
dwarf = "Dwarf"

# Game Loop
while True:

	# (Re)Initialize values
	wizard_hp = 70
	elf_hp = 100
	human_hp = 150
	dwarf_hp = 80

	wizard_damage = 150
	elf_damage = 100
	human_damage = 20
	dwarf_damage = 50

	dragon_hp = 300
	dragon_damage = 50

	# Character selection
	while True:

		# Input from user
		print("1) Wizard")
		print("2) Elf")
		print("3) Human")
		print("4) Dwarf")
		print("5) [EXIT]")
		character = input("Choose your character: ")

		if character == "1" or character.lower() == "wizard":
			my_character = wizard
			my_hp = wizard_hp
			my_damage = wizard_damage
			break

		elif character == "2" or character.lower() == "elf":
			my_character = elf
			my_hp = elf_hp
			my_damage = elf_damage
			break

		elif character == "3" or character.lower() == "human":
			my_character = human
			my_hp = human_hp
			my_damage = human_damage
			break

		elif character == "4" or character.lower() == "dwarf":
			my_character = dwarf
			my_hp = dwarf_hp
			my_damage = dwarf_damage
			break

		elif character == "5":
			print("\nExiting the game...")
			exit()
		
		else:
			print("Unknown character...")

	print("You have chosen the character:", my_character)
	print("Health:", my_hp)
	print("Damage:", my_damage, "\n")

	# Battle
	while True:

		# Character attack
		dragon_hp = dragon_hp - my_damage
		print("The", my_character, "damaged the Dragon!")
		print("The Dragon's health is now:", dragon_hp)
		print()

		if dragon_hp <= 0:
			print("The Dragon has lost the battle.")
			break
		
		# Dragon attack
		my_hp = my_hp - dragon_damage
		print("The Dragon strikes back at " + my_character + ".")
		print("The " + my_character + "'s health is now:", my_hp)
		print()

		if my_hp <= 0:
			print("The", my_character, "has lost the battle.")
			break
	
	# Continue playing 
	play_more = input("\nPlay again? (y/N) ")
	
	if play_more.lower() == "y":
		continue
	else:
		print("Thanks for playing!")
		break
		