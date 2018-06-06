"""
The file contains tests for assignment #9 project Card class

Each test is commented with the test description clearly (hopefully) showing what the test does
"""

import unittest
from card import Card

class CardTest(unittest.TestCase):

    """
    Test that user cannot initialize a Card with wrong type supplied as rank
    the code is expected to throw TypeError
    """
    def test_cannot_init_with_wrong_type_rank(self):
        self.assertRaises(TypeError, Card, "11", "s")

    """
    Test that user cannot initialize a Card with wrong type supplied as suit
    the code is expected to throw TypeError
    """
    def test_cannot_init_with_wrong_type_suit(self):
        self.assertRaises(TypeError, Card, 11, 5)

    """
    Test that user cannot initialize a Card with invalid rank
    the code is expected to throw ValueError
    """
    def test_cannot_init_with_invalid_rank(self):
        self.assertRaises(ValueError, Card, 14, "s")

    """
    Test that user cannot initialize a Card with invalid suit
    the code is expected to throw ValueError
    """
    def test_cannot_init_with_invalid_suit(self):
        self.assertRaises(ValueError, Card, 10, "j")

    """
    Test that user can initialize a Card object with all possible
    valid suit and rank
    """
    def test_can_be_initialized_with_all_possible_values(self):
        possible_ranks = list(range(1, 13))
        possible_suits = ["d", "c", "h", "s"]
        for rank in possible_ranks:
            for suit in possible_suits:
                self.assertIsNotNone(Card(rank, suit))

    """
    Test that Ace card BJ value is equal 1
    """
    def test_bj_value_for_ace(self):
        ace_card = Card(1, "s")
        self.assertEqual(ace_card.bj_value(), 1)

    """
    Test that any face card has BJ value of 10
    """
    def test_bj_value_for_face_cards(self):
        # Jack / Queen / King
        face_cards = [Card(11, "s"), Card(12, "s"), Card(13, "s")]
        for card in face_cards:
            self.assertEqual(card.bj_value(), 10)

    """
    Test that any non-face and not Ace card has BJ value equal to it's value
    """
    def test_non_per_value_cards(self):
        cards = [Card(x, "s") for x in range(2, 11)]
        for card in cards:
            self.assertEqual(card.bj_value(), card.get_rank())

    """
    Test that a random card can be retrieved
    """
    def test_can_init_random_card(self):
        random_card = Card.get_random()
        assert isinstance(random_card, Card)


if __name__ == '__main__':
    unittest.main()