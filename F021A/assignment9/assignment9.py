"""
The main application that thoroughly tests class Hand
"""

from hand import Hand

new_hand = Hand(3)
print(new_hand)
print(new_hand.bj_value())
file_name = 'testing.json'
new_hand.save(file_name)
reloaded_hand = Hand.load_from_disk(file_name)
print(reloaded_hand)
print(reloaded_hand.bj_value())
print("\n Adding a new card: \n")
new_hand.hit_me()
print(new_hand)
print(new_hand.bj_value())
new_hand.save(file_name)
newest_hand = Hand.load_from_disk(file_name)
print(newest_hand)
print(newest_hand.bj_value())