"""
The program is
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