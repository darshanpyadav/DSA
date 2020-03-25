'''
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.
'''


# Problem similar to compression
def countAndSay(n):
    if n == 1:
        return 1
    n = str(countAndSay(n-1))
    res, count = "", 1

    for i in range(1, len(n)):
        if n[i] == n[i-1]:
            count += 1
        else:
            res += str(count) + n[i-1]
            count = 1
    res += str(count) + n[-1]
    return int(res)
    
    
print(countAndSay(8))
