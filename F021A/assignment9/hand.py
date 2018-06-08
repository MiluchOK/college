"""
Object of class Hand represents a hand of cards and so one object stores a number of Card objects
"""

import functools
from card import Card


class Hand:
	# The constructor takes `numCardsInHand` as param
	# numCardsInHand is specifying how many cards you want inside the hand
	def __init__(self, num_cards_in_hand):
		self.cards = [Card.get_random() for i in range(num_cards_in_hand)]

	# Add a new random card to hand
	def hit_me(self):
		new_card = Card.get_random()
		self.cards.append(new_card)

	def bj_value(self):

		return functools.reduce((lambda x, y: x + y.bj_value()), self.cards, 0)

	def __str__(self):
		return functools.reduce((lambda x, y: x + str(y) + "\n"), self.cards, "")
