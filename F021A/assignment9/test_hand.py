"""
The file contains tests for assignment #9 project Hand project

Each test is commented with the test description clearly (hopefully) showing what the test does
"""

import unittest
from hand import Hand
from card import Card
from functools import reduce


class HandTest(unittest.TestCase):
	"""Test that user can initialize a hand with specific amount of cards in"""

	def test_can_init_a_hand(self):
		expected_size = 10
		target_hand = Hand(expected_size)
		self.assertEqual(len(target_hand.cards), expected_size)

	"""Test that user can get hand bj value"""

	def test_can_get_bj_value_of_hand(self):
		target_hand = Hand(3)
		self.assertEqual(target_hand.bj_value(),
						 target_hand.cards[0].bj_value() +
						 target_hand.cards[1].bj_value() +
						 target_hand.cards[2].bj_value()
						 )

	"""Test that user can get hand string representation"""

	def test_can_get_hand_as_string(self):
		target_hand = Hand(3)
		actual_hand_str = str(target_hand)
		expected_hand_str = "{}\n{}\n{}\n".format(str(target_hand.cards[0]),
												str(target_hand.cards[1]),
												str(target_hand.cards[2]))
		self.assertEqual(actual_hand_str, expected_hand_str)

	"""Test that user can add a random card by calling hit_me() method"""

	def test_can_add_a_random_card(self):
		target_hand = Hand(2)
		size_befor_hit = len(target_hand.cards)
		target_hand.hit_me()
		added_card = target_hand.cards[-1]
		self.assertEqual(len(target_hand.cards), size_befor_hit + 1)
		self.assertIsInstance(added_card, Card)


if __name__ == '__main__':
	unittest.main()
