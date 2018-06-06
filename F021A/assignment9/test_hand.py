"""
The file contains tests for assignment #9 project Hand project

Each test is commented with the test description clearly (hopefully) showing what the test does
"""

import unittest
from hand import Hand


class HandTest(unittest.TestCase):
	"""Test that user can initialize a hand"""

	def test_can_init_a_hand(self):
		target_hand = Hand(2)
		assert target_hand.bj_value(), target_hand.cards[0].bj_value() + target_hand.cards[1].bj_value()


if __name__ == '__main__':
	unittest.main()
