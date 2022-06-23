#simulate the 31 card game in python
import random
#begin by creating a dictionary for a deck of cards
card_deck = {}
suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
for suit in suits:
	card_deck[suit] = cards
#create player profile class
class Player:
	personality = ["Conservative", "Moderate", "Risk-Taker"]
	def __init__(self,name):
		self.name = name
		self.personality = random.choice(Player.personality)

Player1 = Player("Player1")
print(Player1.personality)