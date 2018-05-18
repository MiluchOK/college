"""
The file contains tests for assignment #6 project

Each test is commented with the test description clearly (hopefully) showing what the test does
"""

import unittest
from assignment6 import Card

class Assignment6Test(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()