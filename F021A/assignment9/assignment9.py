"""
The main application that thoroughly tests class Hand
"""

from hand import Hand

new_hand = Hand(10)
print(new_hand)
print(new_hand.bj_value())
file_name = 'testing.json'
new_hand.save(file_name)
reloaded_hand = Hand.load_from_disk(file_name)
print(reloaded_hand.cards)
print(reloaded_hand)
print(reloaded_hand.bj_value())
#
#
# print("\n Adding a new card: \n")
#
# new_hand.hit_me()
# print(new_hand)
# print(new_hand.bj_value())
#
# print("\n Making a new Hand: \n")
# very_new_hand = Hand(100)
# print(very_new_hand)
# print(very_new_hand.bj_value())


