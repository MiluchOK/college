import unittest
from assignment3 import magic_hash_merge


class Assignment3Test(unittest.TestCase):

    def test_merges_unique_hashes(self):
        hash1 = {'a': 'b'}
        hash2 = {'f': 'c'}
        result = magic_hash_merge(hash1, hash2)
        self.assertDictEqual(result, {'a': 'b', 'f': 'c'})

    # Same key (array - not array)
    def test_merges_hash_with_repeating_keys_1(self):
        hash1 = {'a': ['b', 'c']}
        hash2 = {'a': 'v'}
        result = magic_hash_merge(hash1, hash2)
        self.assertDictEqual(result, {'a': ['b', 'c', 'v']})

    # Same key (not array - array)
    def test_merges_hash_with_repeating_keys_2(self):
        hash1 = {'a': 'b'}
        hash2 = {'a': ['c', 'v']}
        result = magic_hash_merge(hash1, hash2)
        self.assertDictEqual(result, {'a': ['b', 'c', 'v']})

    # Same key (array - array)
    def test_merges_hash_with_repeating_keys_3(self):
        hash1 = {'a': ['b', 'c']}
        hash2 = {'a': ['v', 'n']}
        result = magic_hash_merge(hash1, hash2)
        self.assertDictEqual(result, {'a': ['b', 'c', 'v', 'n']})

    # Same key (not array - not array)
    def test_merges_hashes_with_repeating_keys_4(self):
        hash1 = {'a': 'b'}
        hash2 = {'a': 'c'}
        result = magic_hash_merge(hash1, hash2)
        self.assertDictEqual(result, {'a': ['b', 'c']})

    def test_integration_test_from_assignment_example(self):
        hash1 = {'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer', 'wine'],
                             'dessert': 'ice cream'}
        hash2 = {'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
        hash3 = {'fruit': ['oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'], 'drinks': 'milk'}
        expected_hash = {'meat': ['hamburger', 'chicken'], 'fruit': ['lemons', 'apples', 'oranges', 'bananas'],
                         'vegetables': ['lettuce', 'carrots', 'potatoes'], 'drinks':
                             ['beer', 'wine', 'apple juice', 'orange juice', 'vodka', 'milk'], 'dessert': 'ice cream'}
        result = magic_hash_merge(magic_hash_merge(hash1, hash2), hash3)
        self.assertDictEqual(result, expected_hash)


if __name__ == '__main__':
    unittest.main()
