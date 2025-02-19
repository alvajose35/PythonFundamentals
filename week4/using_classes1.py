class PlayerCL:

	# Class attribute (changing it changes all objects of the class)
	max_hp = 4000

print("CLASS ATTRIBUTES")

player1cl = PlayerCL()
print(player1cl.max_hp)

player2cl = PlayerCL()
print(player2cl.max_hp)

PlayerCL.max_hp = 5000

print(player1cl.max_hp)
print(player2cl.max_hp)


class Player:

	# Instance attributes
	def __init__(self, name, hp):
		self.name = name
		self.hp = hp
		self.score = 0

print("\n=========================")
print("INSTANCE ATTRIBUTES\n")

player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score)
print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score)

player1.hp += 500
player1.score += 10

print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score)
print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score)