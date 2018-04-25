"""
The program takes a whole number as parameter and returns a string containing the number n2wed out in English
"""

# Hash for number - word mapping
num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
             11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
             20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
             80: 'eighty', 90: 'ninety'
             }

# Array for tens
# num2words2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


# The core n2wing algorithm
def n2w(num):
    if num < 0:
        return "minus " + n2w(num * -1)
    elif num == 0:
        return ""
    elif num < 20:
        return num2words[num]
    elif num < 100:
        # Kind of a special kind
        quotient, remainder = divmod(num, 10)
        return num2words[quotient*10] + " " + n2w(remainder)
    elif num < 1000:
        ray = divmod(num, 100)
        mid = " hundred "
        return num2words[ray[0]] + mid + n2w(ray[1])
    elif num < 1000000:
        return broker(num, 1000, "thousand")
    elif num < 1000000000:
        return broker(num, 1000000, "million")


# The broker logic
def broker(num, grouper, gluer):
    quotient, remainder = divmod(num, grouper)
    return n2w(quotient) + (" {} ".format(gluer)) + n2w(remainder)


# The program gateway for input validation and optimizations
def spell(num):
    max_input = 1000000000000
    min_input = max_input * -1

    if num == 0:
        return "zero"
    elif num > max_input:
        raise ValueError("Invalid input. The value should be no more than {}".format(max_input))
    elif num < min_input:
        raise ValueError("Invalid input. The value should be no less than {}.".format(min_input))
    else:
        return n2w(num)
