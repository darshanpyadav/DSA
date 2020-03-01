'''
Consider the following 6 activities
sorted by by finish time.
start[]  =  {1, 3, 0, 5, 8, 5};
finish[] =  {2, 4, 6, 7, 9, 9};
A person can perform at most four activities. The
maximum set of activities that can be executed
is {0, 1, 3, 4} [ These are indexes in start[] and
                            finish[] ]
'''

# sort on finished time and then do this


def activity(s, e):
    r = 1
    j = 0
    for i in range(1, len(s)):
        if s[i] >= e[j]:
            r += 1
            j = i
    print(r)


activity([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9])


# O(n) if inputs are sorted
# O(n*logN) to sort inputs + to execute the function
