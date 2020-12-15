def canRepresentBST(pre):
    s = []
    root = float('-inf')
    for value in pre:
        if value < root:
            return 0
        while len(s) > 0 and s[-1] < value:
            root = s.pop()
        s.append(value)
    return 1


print(canRepresentBST([5,3,2,1,4,7,6,10]))