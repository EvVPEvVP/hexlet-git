def Football(F: list, N: int) -> bool:

    F3 = F.copy()
    F4 = F.copy()
    F3.sort(reverse=True)
    F4.sort(reverse=False)
    if len(F) == 1 or F4 == F:
        return False
    if F3 == F:
        return True

    for i in range(len(F)):
        if i == (len(F) - 1):
            break
        if F[i] > F[i + 1]:
            x = F[i:i + len(F)]
            minx = min(x)
            break
    Index = F.index(minx)
    F2 = F.copy()
    F2[i], F2[Index] = F2[Index], F2[i]
    F1 = F.copy()
    F1.sort(reverse=False)

    if F2 == F1:
        return True

    x2 = x.copy()
    x2.sort(reverse=True)
    for j in range(len(x)):
        if j == (len(x) - 1):
            break
        if x == x2:
            x1 = x.copy()
            break
        if x[j] < x[j + 1]:
            x1 = x[0:j + 1]
            x1.sort(reverse=False)
            break

    for j in range(j + 1, len(x)):
        if x == x2:
            break
        x1.append(x[j])

    for k in range(i):
        x1.append(F[k])
    x1 = x1[-i:] + x1[:-i]

    if x1 == F1:
        return True
    return  False
