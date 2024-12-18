def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transposed = [[0 for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    return transpos