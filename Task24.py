def MatrixTurn(mat: list, M: int, N: int, T: int):

    mat2 = []
    for k in mat:
        x = list(k)
        result1 = []
        for k1 in x:
            result1.append(int(k1))
        mat2.append(result1)

    del result1
    del x

    for j in range(T):
        top = 0
        bottom = M - 1
        left = 0
        right = N - 1
        while left < right and top < bottom:

            prev = mat2[top + 1][left]
            for i in range(left, right + 1):
                curr = mat2[top][i]
                mat2[top][i] = prev
                prev = curr

            top += 1

            for i in range(top, bottom + 1):
                curr = mat2[i][right]
                mat2[i][right] = prev
                prev = curr

            right -= 1

            for i in range(right, left - 1, -1):
                curr = mat2[bottom][i]
                mat2[bottom][i] = prev
                prev = curr

            bottom -= 1

            for i in range(bottom, top - 1, -1):
                curr = mat2[i][left]
                mat2[i][left] = prev
                prev = curr

            left += 1

    for i in range(len(mat2)):
        matrix2 = ''
        for j in mat2[i]:
            matrix2 += str(j)
        mat[i] = matrix2



