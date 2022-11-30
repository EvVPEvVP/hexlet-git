def TransformTransform(a: list, n: int) -> bool:

    b = []
    c = []
    resultlist = []

    for i in range(len(a)):
        for j in range(len(a) - i):
            k = i + j
            for i1 in range(j, k + 1):
                c.append(a[i1])
            b.append(max(c))
            c.clear()

    for i in range(len(b)):
        for j in range(len(b) - i):
            k = i + j
            for i1 in range(j, k + 1):
                c.append(b[i1])
            resultlist.append(max(c))
            c.clear()

    if sum(resultlist) % 2 == 0:
        return True