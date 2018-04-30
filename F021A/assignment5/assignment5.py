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
        if rank not in Card.possible_ranks:
            raise ValueError("Rank must be one of these: {}. You provided: {}"
                             .format(list(Card.possible_ranks.keys()), rank))
        return rank

    # Validator for suit attribute
    #  "d" "c", "h", or "s"
    @staticmethod
    def _validate_suit(suit):
        if suit not in Card.possible_suits:
            raise ValueError("Suit must be on of these: {}. You provided: {}"
                             .format(list(Card.possible_suits.keys()), suit))
        return suit

    # Method for string representation of the card
    def __str__(self):
        return Card.possible_ranks[self.get_rank()] + " of " + Card.possible_suits[self.get_suit()]


if __name__ == '__main__':

    # Build a deck
    deck = []
    for suite_short_name, suite_full_name in Card.possible_suits.items():
        for rank_input, rank_human_readable in Card.possible_ranks.items():
            deck.append(Card(rank_input, suite_short_name))

    # All combinations should be 52 of size
    print("\nBuild a deck of size: {} \n".format(len(deck)))

    for card in deck:
        print("\n")
        print(card)
        print("Rank: {}".format(card.get_rank()))
        print("Suit: {}".format(card.get_suit()))
        print("Blackjack value: {}".format(card.bj_value()))
