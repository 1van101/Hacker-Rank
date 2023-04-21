def flippingMatrix(n, matrix):
    res = 0
    for i in range(n):
        for j in range(n):
            res += max(matrix[i][j], matrix[i][(2*n)-j-1], matrix[(2*n)-i-1][j], matrix[(2*n)-i-1][(2*n)-j-1])
    return res


print(flippingMatrix(2, [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]))
