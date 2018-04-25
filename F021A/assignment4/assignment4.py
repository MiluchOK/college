"""
The program takes a whole number as parameter and returns a string containing the number n2wed out in English
"""

# Map for number - word mapping
num_word_map = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
    80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 1000000: 'million'
}


# The core `number to word` algorithm
# The function takes in a number
# The function returns a human readable string representation of the number
def numbers_to_words(num):
    if num < 0:
        return "negative " + numbers_to_words(num * -1)
    elif num == 0:
        return ""
    elif num < 20:
        return num_word_map[num]
    elif num < 100:
        # A special kind
        quotient, remainder = divmod(num, 10)
        return num_word_map[quotient * 10] + " " + numbers_to_words(remainder)
    elif num < 1000:
        return broker(num, 100)
    elif num < 1000000:
        return broker(num, 1000)
    elif num < 1000000000:
        return broker(num, 1000000)


# The broker logic necessary to know how to group the numbers
# Takes in the original number and the divider
# Returns string representation of the number
def broker(num, grouper):
    gluer = num_word_map[grouper]
    quotient, remainder = divmod(num, grouper)
    return numbers_to_words(quotient) + (" {} ".format(gluer)) + numbers_to_words(remainder)


# IMPORTANT this function is the program entry point, the rest of functions are meant to be private
# The program gateway for input validation and optimizations
# Takes in the original number
# Returns human readable representation of the number
def spell(num):
    max_input = 1000000000
    min_input = max_input * -1

    if num == 0:
        return "zero"
    elif num >= max_input:
        raise ValueError("Invalid input. The value should be no more than {}".format(max_input))
    elif num <= min_input:
        raise ValueError("Invalid input. The value should be no less than {}.".format(min_input))
    else:
        # Not happy about another round of iteration for replacing, feels like patching wholes, but it works
        # relatively well compare to introducing additional logic for preventing double spaces
        return numbers_to_words(num).replace("  ", " ").strip()

