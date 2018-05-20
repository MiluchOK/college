"""
The program builds multiple cards and outputs it's properties
"""

"""
The class is a representation of a a card
"""


class Card:
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

	# Constructor for the Card
	def __init__(self, rank, suit):
		self.rank = Card._validate_rank(rank)
		self.suit = Card._validate_suit(suit)

	# Getter for rank attribute
	def get_rank(self):
		return self.rank

	# Getter for suit attribute
	def get_suit(self):
		return self.suit

	# Return black jack value of the card
	def bj_value(self):
		if self.get_rank() in Card.faces:
			return 10
		else:
			return self.rank

	# Validator for the rank attribute
	@staticmethod
	def _validate_rank(rank):
		if not isinstance(rank, int):
			raise TypeError("Rank must be an integer.")

		if rank not in Card.possible_ranks:
			raise ValueError("Rank must be one of these: {}. You provided: {}"
							 .format(list(Card.possible_ranks.keys()), rank))
		return rank

	# Validator for suit attribute
	#  "d" "c", "h", or "s"
	@staticmethod
	def _validate_suit(suit):
		if not isinstance(suit, str):
			raise TypeError("Suit must be a string.")

		if suit not in Card.possible_suits:
			raise ValueError("Suit must be on of these: {}. You provided: {}"
							 .format(list(Card.possible_suits.keys()), suit))
		return suit

	# Method for string representation of the card
	def __str__(self):
		return Card.possible_ranks[self.get_rank()] + " of " + Card.possible_suits[self.get_suit()]

	# Private method just for lazy printing on the submission testing phase
	def debug_representation(self):
		# str(valid_card) + "\nRank: {}".format(self.get_rank()) + "\nSuit: {}".format(self.get_suit()) + "\nBlackjack value: {}".format(self.bj_value())
		return "\n{card}\nRank: {rank}\nSuit: {suit}\nBlackjack value: {bj_value}".format(card=self,
																						  rank=self.get_rank(),
																						  suit=self.get_suit(),
																						  bj_value=self.bj_value())


if __name__ == '__main__':
	# IMPORTANT All those test cases are properly tested in the unittests file that is attached to the submission
	# I am adding the following code just for good measure

	def get_random_suit():
		return list(Card.possible_suits.keys())[0]


	def get_random_rank():
		return list(Card.possible_ranks.keys())[0]


	valid_card = Card(get_random_rank(), get_random_suit())

	invalid_cards = [
		# Card with wrong Rank type
		{
			'rank': '1',
			'suit': get_random_suit(),
			'expected_error': TypeError
		},

		# Card with invalid rank
		{
			'rank': 30,
			'suit': get_random_suit(),
			'expected_error': ValueError
		},

		# Card with wrong suit type
		{
			'rank': get_random_rank(),
			'suit': 1,
			'expected_error': TypeError
		},

		# Card with invalid suit
		{
			'rank': 20,
			'suit': get_random_suit(),
			'expected_error': ValueError
		}
	]

	# Main printing code
	print(valid_card.debug_representation())
	for invalid_card in invalid_cards:
		try:
			card = Card(invalid_card['rank'], invalid_card['suit'])
			raise AssertionError("An invalid card have successfully been initialized. {}"
								 .format(card.debug_representation()))
		except AssertionError as exc:
			raise exc
		except Exception as exc:
			actual_exc = type(exc)
			expected_exc = invalid_card['expected_error']
			if actual_exc != expected_exc:
				raise AssertionError("Wrong exception is raised. The exception raised is: {}. \n But expected {}"
									 .format(actual_exc, expected_exc))
			print("Initialization of {} prevented with error: {}".format(invalid_card, invalid_card['expected_error']))


"""
Ace of Heart
Rank: 1
Suit: h
Blackjack value: 1
Initialization of {'expected_error': <type 'exceptions.TypeError'>, 'rank': '1', 'suit': 'h'} prevented with error: <type 'exceptions.TypeError'>
Initialization of {'expected_error': <type 'exceptions.ValueError'>, 'rank': 30, 'suit': 'h'} prevented with error: <type 'exceptions.ValueError'>
Initialization of {'expected_error': <type 'exceptions.TypeError'>, 'rank': 1, 'suit': 1} prevented with error: <type 'exceptions.TypeError'>
Initialization of {'expected_error': <type 'exceptions.ValueError'>, 'rank': 20, 'suit': 'h'} prevented with error: <type 'exceptions.ValueError'>
"""