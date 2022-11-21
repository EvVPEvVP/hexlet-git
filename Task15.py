def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str) ->bool:

    s1 = S1.split()
    s2 = S2.split()

    if (H2*W2) > (H1*W1):
        return False

    for k in range(H1):
        for k1 in range(W1):
            count = 0
            for i in range(H1):
                for j in range(W1):
                    if H2 > i and W2 > j and (j + k1) <= (W1 - 1) and (i + k) <= (H1 - 1) and s2[i][j] == s1[i + k][j + k1]:
                        count += 1
                    if count == (H2 * W2):
                        return True
    return False