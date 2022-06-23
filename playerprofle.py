#create player profile class
import random
class Player:
	personality = ["Conservative", "Moderate", "Risky"]
	def __init__(self,name):
		self.name = name
		self.personality = random.choice(Player.personality)

Player1 = Player("Player1")
print(Player1.personality)

#test initialization of a player2

Player2 = Player("Player2")
print(Player2.personality)