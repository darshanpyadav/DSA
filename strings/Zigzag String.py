'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
 this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **
ABCD, 2 can be written as

A....C
...B....D
and hence the answer would be ACBD.
'''
from collections import defaultdict


def convert(string, integer):
    if integer == 1:
        return string

    d = defaultdict(lambda: "")
    d.fromkeys(range(integer))
    # generate palindrome sequence
    i, fwd = 0, 1
    for val in string:
        d[i] += val
        if fwd:
            i += 1
            if i == integer:
                i -= 2
                fwd = 0
        else:
            i -= 1
            if i == -1:
                i += 2
                fwd = 1
    res = ""
    for i in range(integer):
        res += d[i]
    return res


A = "PAYPALISHIRING"
B = 3
A = "ABCD"
B = 2
print(convert(A, B))
