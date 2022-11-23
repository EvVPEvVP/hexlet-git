def ShopOLAP(N: int, items: str) -> str:

    items1 = items.splitlines()

    b = []
    b1 = []
    b2 = []
    result = []
    spisok = []

    for i in items1:
        y = []
        x = i.partition(' ')[0]
        x1 = i.partition(' ')[2]
        y.append(x)
        y.append(int(x1))
        b.append(y)
    for i1 in b:
        b1.append(i1[0])
        b2.append(i1[1])
    for j in range(len(b1)):
        sum = 0
        result1 = []
        if b1.count(b1[j]) == 1:
            result1.append(b1[j])
            result1.append(b2[j])
            result.append(result1)
        if b1.count(b1[j]) > 1 and b1[j] not in spisok:
                z = [i for i, v in enumerate(b1) if v == b1[j]]
                for k in z:
                    sum += b2[k]
                result1.append(b1[j])
                result1.append(sum)
                result.append(result1)
                spisok.append(b1[j])
    result.sort()
    result = sorted(result, key=lambda x: (x[1]), reverse=True)

    resultstring = ''

    for k1 in range(len(result)):
        resultstring += result[k1][0] + ' ' + str(result[k1][1]) + '\n'
    return resultstring