def native_pattern_search(txt, pat):
    pat_len = len(pat)
    txt_len = len(txt)
    search = []
    for i in range(txt_len - pat_len + 1):
        m = i
        for j in range(pat_len):
            if pat[j] == txt[m]:
                m += 1
            else:
                break
        else:
            search.append(i)
    print(search)


native_pattern_search("AABAACAADAABAABA", "AABA")
# native_pattern_search("THIS IS A TEST TEXT", "TEST")


# Best case when no pattern found : O(txt_len)
# Worst case: when pattern is at end or every index has pattern: O(txt_len*(txt_len-pat_len))


# Other searches

# Using re
import re
search = [m.start() for m in re.finditer("(?=AABA)", "AABAACAADAABAABA")]
print(search)


# Using s.find()

def pat(s, p):
    search = []
    i = s.find(p)
    while i != -1:
        search.append(i)
        i = s.find(p, i+1)
    print(search)

pat("AABAACAADAABAABA", "AABA")


#  Using window of len(pat) to move
txt = "AABAACAADAABAABA"
pat = "AABA"
pat_len = len(pat)
txt_len = len(txt)
s = []
for i in range(txt_len - pat_len + 1):
    if txt[i:i+pat_len] == pat:
        s.append(i)
print(s)