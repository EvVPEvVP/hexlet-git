def ConquestCampaign(N: int,M: int,L: int,battalion: list) -> int:
    a = []
    L1 = str(L)
    sum = 0

    if N == 1 and M == 1:
        return 1

    for i in range(N):
        b = []
        for j in range(M):
            b.append(1)
        a.append(b)

    for k in range(len(battalion)):
        if k % 2 == 0:
            a[battalion[k] - 1][battalion[k + 1] - 1] = 0
    day = 1
    for p in range(N):
        for s in range(M):
            if a[p][s] != 0:
                sum += 1
    if sum == 0:
        return day

    for z in range(N*M):
        sum = 0
        for x in range(N):
            for y in range(M):
                if M == 1 and a[x][y] == 0:
                    if x == 0:
                        if a[x + 1][y] != 0:
                            a[x + 1][y] = L1
                    if x == N - 1:
                        if a[x - 1][y] != 0:
                            a[x - 1][y] = L1
                    else:
                        if a[x - 1][y] != 0:
                            a[x - 1][y] = L1
                        if a[x + 1][y] != 0:
                            a[x + 1][y] = L1
                elif N == 1 and a[x][y] == 0:
                    if y == 0:
                        if a[x][y + 1] != 0:
                            a[x][y + 1] = L1
                    if y == M - 1:
                        if a[x][y - 1] != 0:
                            a[x][y - 1] = L1
                    else:
                        if a[x][y - 1] != 0:
                            a[x][y - 1] = L1
                        if a[x][y + 1] != 0:
                            a[x][y + 1] = L1
                elif x == 0 and a[x][y] == 0:
                    if y == 0:
                        if a[x][y + 1] != 0:
                            a[x][y + 1] = L1
                        if a[x + 1][y] != 0:
                            a[x + 1][y] = L1
                    if y == M - 1:
                        if a[x][y - 1] != 0:
                            a[x][y - 1] = L1
                        if a[x + 1][y] != 0:
                            a[x + 1][y] = L1
                    else:
                        if a[x][y - 1] != 0:
                            a[x][y - 1] = L1
                        if a[x][y + 1] != 0:
                            a[x][y + 1] = L1
                        if a[x + 1][y] != 0:
                            a[x + 1][y] = L1
                elif x == N - 1 and a[x][y] == 0:
                    if y == 0:
                        if a[x - 1][y] != 0:
                            a[x - 1][y] = L1
                        if a[x][y + 1] != 0:
                            a[x][y + 1] = L1
                    if y == M - 1:
                        if a[x][y - 1] != 0:
                            a[x][y - 1] = L1
                        if a[x - 1][y] != 0:
                            a[x - 1][y] = L1
                    else:
                        if a[x][y - 1] != 0:
                            a[x][y - 1] = L1
                        if a[x - 1][y] != 0:
                            a[x - 1][y] = L1
                        if a[x][y + 1] != 0:
                            a[x][y + 1] = L1
                elif y == 0 and a[x][y] == 0:
                    if a[x + 1][y] != 0:
                        a[x + 1][y] = L1
                    if a[x][y + 1] != 0:
                        a[x][y + 1] = L1
                    if a[x - 1][y] != 0:
                        a[x - 1][y] = L1
                elif y == M - 1 and a[x][y] == 0:
                    if a[x + 1][y] != 0:
                        a[x + 1][y] = L1
                    if a[x][y - 1] != 0:
                        a[x][y - 1] = L1
                    if a[x - 1][y] != 0:
                        a[x - 1][y] = L1
                elif a[x][y] == 0:
                    if a[x][y - 1] != 0:
                        a[x][y - 1] = L1
                    if a[x - 1][y] != 0:
                        a[x - 1][y] = L1
                    if a[x][y + 1] != 0:
                        a[x][y + 1] = L1
                    if a[x + 1][y] != 0:
                        a[x + 1][y] = L1

        for x1 in range(N):
            for y1 in range(M):
                if a[x1][y1] == L1:
                    a[x1][y1] = 0
        day +=1
        x3 = []
        for x2 in a:
            x3.extend(x2)
            if 1 in x3:
                sum +=1
                x3.clear()
        if sum == 0:
            break
    return day



