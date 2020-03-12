def generate_spiral_matrix(A):
    mat = [[None]*A for _ in range(A)]
    count = 1
    row_start, col_start = 0, 0
    row_end, col_end = A-1, A-1

    while row_start <= row_end and col_start <= col_end:
        # left to right
        for i in range(col_start, col_end+1):
            mat[row_start][i] = count
            count += 1
        row_start += 1

        # top to bottom
        for i in range(row_start, row_end+1):
            mat[i][col_end] = count
            count += 1
        col_end -= 1

        # right to left
        for i in range(col_end, col_start-1, -1):
            mat[row_end][i] = count
            count += 1
        row_end -= 1

        # bottom to top
        for i in range(row_end, row_start-1, -1):
            mat[i][col_start] = count
            count += 1
        col_start += 1

    return mat


print(generate_spiral_matrix(5))
