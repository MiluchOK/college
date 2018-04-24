

# def n2w(n):

    # int_map = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    #            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    #            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    #            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    #            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
    #            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
    #            90: 'ninety'}
    #
    # try:
    #     return int_map[n]
    # except KeyError:
    #     try:
    #         return int_map[n - n % 10] + ' ' + int_map[n % 10].lower()
    #     except KeyError:
    #         raise RuntimeError('Number out of range {}'.format(n))


num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def n2w(num):
    if num < 0:
        print('1')
        return "minus " + n2w(num * -1)
    if num == 0:
        print('2')
        return ""
    if num < 20:
        print('3')
        return (num2words[num])
    elif num < 100:
        print('4')
        ray = divmod(num,10)
        return (num2words2[ray[0]-2]+" "+n2w(ray[1]))
    elif num <1000:
        print('5')
        ray = divmod(num,100)
        mid = " hundred "
        return(num2words[ray[0]]+mid+n2w(ray[1]))
    elif num < 1000000:
        print('6')
        ray = divmod(num, 1000)
        mid = " thousand "
        return(n2w(ray[0])+ mid +n2w(ray[1]))
    elif num < 1000000000:
        print('7')
        ray = divmod(num, 1000000)
        mid = " million "
        return(n2w(ray[0])+ mid +n2w(ray[1]))

print(n2w(9999))
