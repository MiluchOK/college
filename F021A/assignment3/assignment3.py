"""
The program combines several dictionaries into a new dictionary with all the keys of the original dictionaries.
If a key appears in more than one input dictionary, the value corresponding to that key in the new dictionary will
be a list containing all the values encountered in the input dictionaries that correspond to that key.
 If a key appears in only one of the input dictionaries, the value for that key in the resulting dictionary will
be exactly as it was in the input dictionary.
"""


def magic_hash_merge(hash1, hash2):
    result = hash1.copy()
    for key, value in hash2.items():
        if key in result:
            result[key] = merge_values(hash1[key], value)
        else:
            result[key] = value

    return result


def merge_values(value1, value2):
    if not isinstance(value1, list):
        value1 = [value1]

    if not isinstance(value2, list):
        value2 = [value2]

    return value1 + value2


# Test Case #1
hash1 = {'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer', 'wine'],
                             'dessert': 'ice cream'}
hash2 = {'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
hash3 = {'fruit': ['oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'], 'drinks': 'milk'}
print(magic_hash_merge(magic_hash_merge(hash1, hash2), hash3))


# Test Case #2
hash1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v5', 'k4': 'v10'}
hash2 = {'k1': 'v3', 'k2': 'v4', 'k3': 'v6', 'k5': 'v11'}
hash3 = {'k1': 'v7', 'k2': 'v8', 'k3': 'v9', 'k6': 'v12'}
print(magic_hash_merge(magic_hash_merge(hash1, hash2), hash3))

# Test Case #3 ((non-array / array), (array / non-array), (array / array), (non-array / non-array) )
hash1 = {'k1': 'v1', 'k2': ['v1', 'v2'], 'k3': ['v1', 'v2'], 'k4': 'v1'}
hash2 = {'k1': ['v3', 'v4'], 'k2': 'v3', 'k3': ['v3', 'v4'], 'k4': 'v2'}
hash3 = {'k2': 'v1', 'k1': ['v1', 'v2']}
print(magic_hash_merge(magic_hash_merge(hash1, hash2), hash3))

"""
{'fruit': ['apples', 'lemons', 'oranges', 'bananas'], 'meat': ['chicken', 'hamburger'], 'vegetables': ['potatoes', 'lettuce', 'carrots'], 'drinks': ['beer', 'wine', 'apple juice', 'orange juice', 'vodka', 'milk'], 'dessert': 'ice cream'}
{'k1': ['v1', 'v3', 'v7'], 'k2': ['v2', 'v4', 'v8'], 'k3': ['v5', 'v6', 'v9'], 'k4': 'v10', 'k5': 'v11', 'k6': 'v12'}
{'k1': ['v1', 'v3', 'v4', 'v1', 'v2'], 'k2': ['v1', 'v2', 'v3', 'v1'], 'k3': ['v1', 'v2', 'v3', 'v4'], 'k4': ['v1', 'v2']}
"""