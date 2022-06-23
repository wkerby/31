#create player profile class
class Player:
	personality = ["Conservative", "Moderate", "Risk-Taker"]
	def __init__(self,name):
		self.name = name
		self.personality = random.choice(Player.personality)

Player1 = Player("Player1")
print(Player1.personality)
