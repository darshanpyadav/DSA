# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 20/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************


def matrix_product(p):
    """Return m and s.

    m[i][j] is the minimum number of scalar multiplications needed to compute the
    product of matrices A(i), A(i + 1), ..., A(j).

    s[i][j] is the index of the matrix after which the product is split in an
    optimal parenthesization of the matrix product.

    p[0... n] is a list such that matrix A(i) has dimensions p[i - 1] x p[i].
    """
    n = len(p)
    # len(p) = number of matrices + 1

    m = [[-1]*n for _ in range(n)]
    s = [[-1]*n for _ in range(n)]

    for l in range(1, n):
        m[l][l] = 0
    for l in range(2, n):
        for i in range(1, n-l+1):
            j = i + l - 1
            q = float('inf')
            for k in range(i, j):
                temp = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if temp < q:
                    s[i][j] = k
                    q = temp
            m[i][j] = q

    return m, s


def print_expression(s, i, j):
    """Print the optimal parenthesization of the matrix product A(i) x
    A(i + 1) x ... x A(j).

    s[i][j] is the index of the matrix after which the product is split in an
    optimal parenthesization of the matrix product.
    """
    if i == j:
        print(f'A[{i}]', end="")
        return
    k = s[i][j]
    print("(", end="")
    print_expression(s, i, k)
    print_expression(s, k+1, j)
    print(")", end="")


if __name__ == "__main__":
    p = []
    # n = int(input("Enter number of matrices"))
    # for i in range(n):
    #     p.append(int(input("Enter the rows of " + str(i+1) + "matrix")))
    # p.append(int(input("Enter the column of last matrix")))
    n = 3
    p = [10, 100, 5, 50]
    m, s = matrix_product(p)
    print('The number of scalar multiplications needed:', m[1][n])
    print('Optimal parenthesization: ', end='')
    print_expression(s, 1, n)
