'''
Print concentric rectangular pattern in a 2d matrix.
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.
Output:

4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
Example 2:

Input: A = 3.
Output:

3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

You will be given A as an argument to the function you need to implement, and you need to return a 2D array.
'''


def prettyPrint(A):
    r = []
    num = ""
    if A == 1:
        return [1]

    for i in range(A, 0, -1):
        num += str(i)

    num, add_num = int(num), "0"

    for i in range(A):
        num += int(add_num)
        temp = str(num) + str(num)[A-2::-1]
        r.append(list(map(int, temp)))
        add_num += "1"

    r = r[::-1] + r[1:]
    return r


print(prettyPrint(4))
