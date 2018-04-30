"""
The program builds multiple cards and outputs it's properties
"""


class Card:
    possible_suits = ["d" "c", "h", "s"]
    possible_ranks = list(range(1, 14))
    faces = list(range(11, 14))

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
        if rank not in Card.possible_ranks:
            raise ValueError("Rank must be one of these: {}".format(Card.possible_ranks))
        return rank

    @staticmethod
    # Validator for suit attribute
    #  "d" "c", "h", or "s"
    def _validate_suit(suit):
        if suit not in Card.possible_suits:
            raise ValueError("Suit must be on of these: {}".format(Card.possible_ranks))
        return suit
