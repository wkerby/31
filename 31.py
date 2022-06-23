#simulate the 31 card game in python
#begin by creating a dictionary for a deck of cards
card_deck = {}
suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
for suit in suits:
	card_deck[suit] = cards
