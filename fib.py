def fib(up_to_order, num1=0, num2=1):
    up_to_order -= 1
    sum = num1 + num2
    if up_to_order <= 0:
        return sum
    return fib(up_to_order, num2, sum)


def count(word, target_char):
    h = {}
    for char in word:
        if char in h:
            h[char] += 1
        else:
            h[char] = 1

    if target_char in h:
        return h[target_char]
    else:
        return 0


print(count('foosdf', 'f'))
