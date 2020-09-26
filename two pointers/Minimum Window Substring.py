'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".
Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''
from collections import defaultdict


def minWindow(s, t):
    n = len(s)
    slow = 0
    start_index, end_index = float('-inf'), float('inf')
    d = defaultdict(int).fromkeys(t, 0)
    missing = len(t)

    for fast in range(n):
        ele = s[fast]
        if ele in d:
            if d[ele] == 0:
                missing -= 1
            d[ele] += 1
        while missing == 0:
            if fast - slow < end_index - start_index:
                start_index, end_index = slow, fast
            ele = s[slow]
            if ele in d:
                d[ele] -= 1
                if d[ele] == 0:
                    missing += 1
            slow += 1

    return "" if start_index == float('-inf') else s[start_index:end_index+1]


print(minWindow("ADOBECODEBANC", "ABC"))