'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.

Example:

words: ["This", "is", "an", "example", "of", "text", "justification."]

L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
 Note: Each word is guaranteed not to exceed L in length
'''
from math import ceil


def fullJustify(A, B):
    left = B
    res = []
    string = ""

    prev_i, i, start = 0, 0, 0
    while i < len(A):
        if len(A[i]) <= left:
            left -= len(A[i]) + 1
            string += A[i] + " "
            i += 1
        else:
            string = ""
            left = left + 1
            words = i - prev_i
            for m in range(words):
                string += A[prev_i+m] + " "
                try:
                    spaces = ceil(left/(words-1-m))
                    string += " "*spaces
                    left -= spaces
                except Exception:
                    continue
            res.append(string.rstrip(" "))
            left = B
            prev_i = i
            string = ""

    res.append(string.ljust(16))
    return res


A = ["This", "is", "an", "example", "of", "text", "justification", "yes"]
B = 16
# A = [ "What", "must", "be", "shall", "be." ]
# B = 12
print(fullJustify(A, B))
