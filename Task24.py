def MatrixTurn(mat: list, M: int, N: int, T: int):

    mat2 = []
    for k in mat:
        x = list(k)
        result1 = []
        for k1 in x:
            result1.append(int(k1))
        mat2.append(result1)

    mat = mat2.copy()
    del result1
    del x

    for j in range(T):
        top = 0
        bottom = M - 1
        left = 0
        right = N - 1
        while left < right and top < bottom:

            prev = mat[top + 1][left]
            for i in range(left, right + 1):
                curr = mat[top][i]
                mat[top][i] = prev
                prev = curr

            top += 1

            for i in range(top, bottom + 1):
                curr = mat[i][right]
                mat[i][right] = prev
                prev = curr

            right -= 1

            for i in range(right, left - 1, -1):
                curr = mat[bottom][i]
                mat[bottom][i] = prev
                prev = curr

            bottom -= 1

            for i in range(bottom, top - 1, -1):
                curr = mat[i][left]
                mat[i][left] = prev
                prev = curr

            left += 1

    matrix1 = []
    for i in range(len(mat)):
        matrix2 = ''
        for j in range(len(mat[i])):
            matrix2 += str(mat[i][j])
        matrix1.append(matrix2)

    mat = matrix1.copy()




