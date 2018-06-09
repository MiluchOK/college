"""
Object of class Hand represents a hand of cards and so one object stores a number of Card objects
"""

import functools
import json
from card import Card


class Hand:
	def __init__(self, num_cards_in_hand):
		"""
		The constructor takes `numCardsInHand` as param
		numCardsInHand is specifying how many cards you want inside the hand
		:param num_cards_in_hand:
		"""
		self.cards = [Card.get_random() for i in range(num_cards_in_hand)]

	def hit_me(self):
		"""
		Add a new card to hand
		:return: Hand
		"""
		new_card = Card.get_random()
		self.cards.append(new_card)
		return self

	def bj_value(self):
		"""
		Get BJ value for the hand
		:return: integer
		"""
		return functools.reduce((lambda x, y: x + y.bj_value()), self.cards, 0)

	def save(self, filename):
		"""
		Save the hand as a json in a file
		:param filename:
		:return: self
		"""
		with open(filename, 'w') as outfile:
			json.dump(self.to_export(), outfile)
		return self

	@staticmethod
	def load_from_disk(filename):
		"""
		Load hand object from the file
		:param filename:
		:return: Hand object loaded from file
		"""
		with open(filename) as f:
			loaded_cards = json.load(f)
		hand = Hand(0)
		hand.cards = list(map(lambda x: Card(x['rank'], x['suit']), loaded_cards))
		return hand

	# Get String representation of the Hand
	def __str__(self):
		"""
		:return: String representation of the object
		"""
		return functools.reduce((lambda x, y: x + str(y) + "\n"), self.cards, "")

	def __eq__(self, other):
		"""
		Check equality
		:param other:
		:return: Boolean
		"""
		return self.cards == other.cards

	def to_export(self):
		"""
		Export the object as a hash
		:return: Hash
		"""
		return [card.to_export() for card in self.cards]
