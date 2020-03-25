def compareVersion(A, B):
    for i in range(len(A)):
        if A[i] == ".":
            A = A[:i] + "." + "".join(A[i+1:].split("."))
            break

    for i in range(len(B)):
        if B[i] == ".":
            B = B[:i] + "." + "".join(B[i+1:].split("."))
            break

    A, B = float(A), float(B)
    if A > B:
        return 1
    elif A < B:
        return -1
    else:
        return 0


A = "1.0"
B = "1"
A = "4444371174137455"
B = "5.1.6.8"
print(compareVersion(A, B))