"""
The class is a representation of a a card
"""

import random


class Card:

	"""
		The class is a representation of a a card
	"""

	possible_suits = {
		'd': 'Diamonds',
		'c': 'Clubs',
		'h': 'Heart',
		's': 'Spades'
	}

	possible_ranks = {
		1: 'Ace',
		2: 'Two',
		3: 'Three',
		4: 'Four',
		5: 'Five',
		6: 'Six',
		7: 'Seven',
		8: 'Eight',
		9: 'Nine',
		10: 'Ten',
		11: 'Jack',
		12: 'Queen',
		13: 'King'
	}

	faces = list(range(11, 14))

	def __init__(self, rank, suit):
		"""
		Constructor for the Card
		:param rank:
		:param suit:
		"""
		self.rank = Card._validate_rank(rank)
		self.suit = Card._validate_suit(suit)

	def get_rank(self):
		"""
		Getter for rank attribute
		:return: int
		"""
		return self.rank

	def get_suit(self):
		"""
		Getter for suit attribute
		:return: String
		"""
		return self.suit

	def bj_value(self):
		"""
		Return black jack value of the card
		:return: integer
		"""
		if self.get_rank() in Card.faces:
			return 10
		else:
			return self.rank

	@staticmethod
	def _validate_rank(rank):
		"""
		Validator for the rank attribute
		:param rank:
		:return: integer
		"""
		if not isinstance(rank, int):
			raise TypeError("Rank must be an integer.")

		if rank not in Card.possible_ranks:
			raise ValueError("Rank must be one of these: {}. You provided: {}"
							 .format(list(Card.possible_ranks.keys()), rank))
		return rank

	@staticmethod
	def _validate_suit(suit):
		"""
		Validator for suit attribute
		:param suit:
		:return: String
		"""
		if not isinstance(suit, str):
			raise TypeError("Suit must be a string.")

		if suit not in Card.possible_suits:
			raise ValueError("Suit must be on of these: {}. You provided: {}"
							 .format(list(Card.possible_suits.keys()), suit))
		return suit

	@staticmethod
	def get_random():
		"""
		Generate a random card
		:return: Card
		"""
		return Card(random.choice(list(Card.possible_ranks.keys())), random.choice(list(Card.possible_suits.keys())))

	def __str__(self):
		"""
		Method for string representation of the card
		:return: String
		"""
		return Card.possible_ranks[self.get_rank()] + " of " + Card.possible_suits[self.get_suit()]

	def debug_representation(self):
		"""
		Private method just for lazy printing on the submission testing phase
		:return: String
		"""
		return "\n{card}\nRank: {rank}\nSuit: {suit}\nBlackjack value: {bj_value}".format(card=self,
																						  rank=self.get_rank(),
																						  suit=self.get_suit(),
																						  bj_value=self.bj_value())

	def to_export(self):
		"""
			Export the object as a hash
		"""
		return {'suit': self.suit, 'rank': self.rank}

	def __eq__(self, other):
		return self.suit == other.suit and self.rank == other.rank
