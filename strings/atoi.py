def atoi(string):
    res = 0
    # initialize sign as positive
    sign = 1
    i = 0

    # if number is negative then update sign
    if string[0] == '-':
        sign = -1
        i += 1

    # Iterate through all characters of input string and update result
    for j in range(i, len(string)):
        res = res * 10 + (ord(string[j]) - ord('0'))

    return sign * res
