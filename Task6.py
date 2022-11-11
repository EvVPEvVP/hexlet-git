def PatternUnlock(N: int,hits: list) -> str:

    kod = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    hits1 = []
    sum = 0
    for a in hits:
        hits1.append(a)

    for k in hits:
        if len(hits1) == 1:
            break
        for i1 in kod:
            for i2 in i1:
                if i2 == k:
                    next = hits1[hits1.index(k) + 1]
                    if k == 6 or k == 9 or k == 4 or k == 7:
                        if next == 2:
                            sum += 1.414215
                        else:
                            sum += 1.00000
                    elif k == 1 or k == 3:
                        if next == 5 or next == 8:
                            sum += 1.414215
                        else:
                            sum += 1.00000
                    elif k == 5 or k == 8:
                        if next == 1 or next == 3:
                            sum += 1.414215
                        else:
                            sum += 1.00000
                    else:
                        if next == 6 or next == 9 or next == 4 or next == 7:
                            sum += 1.414215
                        else:
                            sum += 1.00000
        hits1.pop(0)

    sum = round(sum,5)
    sum = str(sum)
    sum = list(sum)

    while '.' in sum or '0' in sum:
        for x in sum:
            if x == '.' or x == '0':
                sum.remove(x)
    length = ''.join(sum)
    return length