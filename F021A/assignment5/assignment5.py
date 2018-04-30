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

    # Print each card and it's properties
    for card in deck:
        print("\n")
        print(card)
        print("Rank: {}".format(card.get_rank()))
        print("Suit: {}".format(card.get_suit()))
        print("Blackjack value: {}".format(card.bj_value()))

"""
OUTPUT:


Build a deck of size: 52 



Ace of Diamonds
Rank: 1
Suit: d
Blackjack value: 1


Two of Diamonds
Rank: 2
Suit: d
Blackjack value: 2


Three of Diamonds
Rank: 3
Suit: d
Blackjack value: 3


Four of Diamonds
Rank: 4
Suit: d
Blackjack value: 4


Five of Diamonds
Rank: 5
Suit: d
Blackjack value: 5


Six of Diamonds
Rank: 6
Suit: d
Blackjack value: 6


Seven of Diamonds
Rank: 7
Suit: d
Blackjack value: 7


Eight of Diamonds
Rank: 8
Suit: d
Blackjack value: 8


Nine of Diamonds
Rank: 9
Suit: d
Blackjack value: 9


Ten of Diamonds
Rank: 10
Suit: d
Blackjack value: 10


Jack of Diamonds
Rank: 11
Suit: d
Blackjack value: 10


Queen of Diamonds
Rank: 12
Suit: d
Blackjack value: 10


King of Diamonds
Rank: 13
Suit: d
Blackjack value: 10


Ace of Clubs
Rank: 1
Suit: c
Blackjack value: 1


Two of Clubs
Rank: 2
Suit: c
Blackjack value: 2


Three of Clubs
Rank: 3
Suit: c
Blackjack value: 3


Four of Clubs
Rank: 4
Suit: c
Blackjack value: 4


Five of Clubs
Rank: 5
Suit: c
Blackjack value: 5


Six of Clubs
Rank: 6
Suit: c
Blackjack value: 6


Seven of Clubs
Rank: 7
Suit: c
Blackjack value: 7


Eight of Clubs
Rank: 8
Suit: c
Blackjack value: 8


Nine of Clubs
Rank: 9
Suit: c
Blackjack value: 9


Ten of Clubs
Rank: 10
Suit: c
Blackjack value: 10


Jack of Clubs
Rank: 11
Suit: c
Blackjack value: 10


Queen of Clubs
Rank: 12
Suit: c
Blackjack value: 10


King of Clubs
Rank: 13
Suit: c
Blackjack value: 10


Ace of Heart
Rank: 1
Suit: h
Blackjack value: 1


Two of Heart
Rank: 2
Suit: h
Blackjack value: 2


Three of Heart
Rank: 3
Suit: h
Blackjack value: 3


Four of Heart
Rank: 4
Suit: h
Blackjack value: 4


Five of Heart
Rank: 5
Suit: h
Blackjack value: 5


Six of Heart
Rank: 6
Suit: h
Blackjack value: 6


Seven of Heart
Rank: 7
Suit: h
Blackjack value: 7


Eight of Heart
Rank: 8
Suit: h
Blackjack value: 8


Nine of Heart
Rank: 9
Suit: h
Blackjack value: 9


Ten of Heart
Rank: 10
Suit: h
Blackjack value: 10


Jack of Heart
Rank: 11
Suit: h
Blackjack value: 10


Queen of Heart
Rank: 12
Suit: h
Blackjack value: 10


King of Heart
Rank: 13
Suit: h
Blackjack value: 10


Ace of Spades
Rank: 1
Suit: s
Blackjack value: 1


Two of Spades
Rank: 2
Suit: s
Blackjack value: 2


Three of Spades
Rank: 3
Suit: s
Blackjack value: 3


Four of Spades
Rank: 4
Suit: s
Blackjack value: 4


Five of Spades
Rank: 5
Suit: s
Blackjack value: 5


Six of Spades
Rank: 6
Suit: s
Blackjack value: 6


Seven of Spades
Rank: 7
Suit: s
Blackjack value: 7


Eight of Spades
Rank: 8
Suit: s
Blackjack value: 8


Nine of Spades
Rank: 9
Suit: s
Blackjack value: 9


Ten of Spades
Rank: 10
Suit: s
Blackjack value: 10


Jack of Spades
Rank: 11
Suit: s
Blackjack value: 10


Queen of Spades
Rank: 12
Suit: s
Blackjack value: 10


King of Spades
Rank: 13
Suit: s
Blackjack value: 10
"""