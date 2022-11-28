def TreeOfLife(H: int, W: int, N: int, tree: list) -> list:

    arr = []

    for i in range(H):
        arr1 = []
        for j in range(W):
            if tree[i][j] == '.':
                arr1.append(0)
            elif tree[i][j] == '+':
                arr1.append(1)
        arr.append(arr1)

    for k in range(N):
        for i in range(H):
            for j in range(W):
                arr[i][j] += 1
        if k % 2 == 0:
            continue
        for i1 in range(H):
            for j1 in range(W):
                if H == 1 and W != 1 and j1 == 0:
                    arr[i1][j1] = 0
                    if arr[i1][j1 + 1] < 3:
                        arr[i1][j1 + 1] = 0
                elif H == 1 and W != 1 and j1 == (W - 1):
                    arr[i1][j1] = 0
                    if arr[i1][j1 - 1] < 3:
                        arr[i1][j1 - 1] = 0
                elif H == 1 and W != 1 and j1 != 0 and j1 != (W - 1):
                    arr[i1][j1] = 0
                    if arr[i1][j1 + 1] < 3:
                        arr[i1][j1 + 1] = 0
                    if arr[i1][j1 - 1] < 3:
                        arr[i1][j1 - 1] = 0
                elif H != 1 and W == 1 and i1 == 0:
                    arr[i1][j1] = 0
                    if arr[i1 + 1][j1] < 3:
                        arr[i1 + 1][j1] = 0
                elif H != 1 and W == 1 and i1 == (H - 1):
                    arr[i1][j1] = 0
                    if arr[i1 - 1][j1] < 3:
                        arr[i1 - 1][j1] = 0
                elif H != 1 and W == 1 and i1 != 0 and i1 != (H - 1):
                    arr[i1][j1] = 0
                    if arr[i1 - 1][j1] < 3:
                        arr[i1 - 1][j1] = 0
                    if arr[i1 + 1][j1] < 3:
                        arr[i1 + 1][j1] = 0
                elif H == 1 and W == 1:
                    arr[i1][j1] = 0
                elif H != 1 and W != 1 and i1 == 0 and j1 == 0 and arr[i1][j1] >= 3:
                    arr[i1][j1] = 0
                    if arr[i1 + 1][j1] < 3:
                        arr[i1 + 1][j1] = 0
                    if arr[i1][j1 + 1] < 3:
                        arr[i1][j1 + 1] = 0
                elif H != 1 and W != 1 and i1 == 0 and j1 == (W - 1) and arr[i1][j1] >= 3:
                    arr[i1][j1] = 0
                    if arr[i1][j1 - 1] < 3:
                        arr[i1][j1 - 1] = 0
                    if arr[i1 + 1][j1] < 3:
                        arr[i1 + 1][j1] = 0
                elif H != 1 and W != 1 and i1 == (H - 1) and j1 == 0 and arr[i1][j1] >= 3:
                    arr[i1][j1] = 0
                    if arr[i1 - 1][j1] < 3:
                        arr[i1 - 1][j1] = 0
                    if arr[i1][j1 + 1] < 3:
                        arr[i1][j1 + 1] = 0
                elif H != 1 and W != 1 and i1 == (H - 1) and j1 == (W - 1) and arr[i1][j1] >= 3:
                    arr[i1][j1] = 0
                    if arr[i1][j1 - 1] < 3:
                        arr[i1][j1 - 1] = 0
                    if arr[i1 - 1][j1] < 3:
                        arr[i1 - 1][j1] = 0
                elif H != 1 and W != 1 and j1 == 0 and arr[i1][j1] >= 3:
                    arr[i1][j1] = 0
                    if arr[i1 - 1][j1] < 3:
                        arr[i1 - 1][j1] = 0
                    if arr[i1 + 1][j1] < 3:
                        arr[i1 + 1][j1] = 0
                    if arr[i1][j1 + 1] < 3:
                        arr[i1][j1 + 1] = 0
                elif H != 1 and W != 1 and j1 == (W - 1) and arr[i1][j1] >= 3:
                    arr[i1][j1] = 0
                    if arr[i1 - 1][j1] < 3:
                        arr[i1 - 1][j1] = 0
                    if arr[i1 + 1][j1] < 3:
                        arr[i1 + 1][j1] = 0
                    if arr[i1][j1 - 1] < 3:
                        arr[i1][j1 - 1] = 0
                elif H != 1 and W != 1 and i1 == 0 and arr[i1][j1] >= 3:
                    arr[i1][j1] = 0
                    if arr[i1][j1 - 1] < 3:
                        arr[i1][j1 - 1] = 0
                    if arr[i1][j1 + 1] < 3:
                        arr[i1][j1 + 1] = 0
                    if arr[i1 + 1][j1] < 3:
                        arr[i1 + 1][j1] = 0
                elif H != 1 and W != 1 and i1 == (H - 1) and arr[i1][j1] >= 3:
                    arr[i1][j1] = 0
                    if arr[i1][j1 - 1] < 3:
                        arr[i1][j1 - 1] = 0
                    if arr[i1][j1 + 1] < 3:
                        arr[i1][j1 + 1] = 0
                    if arr[i1 - 1][j1] < 3:
                        arr[i1 - 1][j1] = 0
                elif H != 1 and W != 1 and arr[i1][j1] >= 3:
                    arr[i1][j1] = 0
                    if arr[i1 - 1][j1] < 3:
                        arr[i1 - 1][j1] = 0
                    if arr[i1][j1 + 1] < 3:
                        arr[i1][j1 + 1] = 0
                    if arr[i1 + 1][j1] < 3:
                        arr[i1 + 1][j1] = 0
                    if arr[i1][j1 - 1] < 3:
                        arr[i1][j1 - 1] = 0

    resultlist = []
    for i in range(H):
        resultstr = ' '
        for j in range(W):
            if arr[i][j] == 0:
                resultstr += '.'
            elif arr[i][j] > 0:
                resultstr += '*'
        resultlist.append(resultstr)
    return resultlist