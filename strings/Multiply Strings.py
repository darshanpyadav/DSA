'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.
For example,
given strings "12", "10", your answer should be “120”.

NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
We will retroactively disqualify such submissions and the submissions will incur penalties.
'''


def multiply(A, B):
    # return str(int(A)*int(B))
    res = 0
    if int(A) < int(B):
        A, B = B, A
    B = B[::-1]
    for i in range(len(B)):
        cur_op = str(int(B[i])*int(A))
        cur_op += "0"*i
        res += int(cur_op)
    return res


print(multiply("121", "100"))
