def BiggerGreater(input: str) -> str:

    input1 = list(input)
    x = 0
    resultlist = []

    for i in range(len(input1) - 1, 0, -1):
        if x == 1:
            break
        for j in range(len(input1) - 1, 0, -1):
            if j < i and input1[i] > input1[j]:
                input1[j], input1[i] = input1[i], input1[j]
                x = 1
                break

    if x == 1:
        y = input1[j + 1:]
        y.sort()
        result = input1[:j + 1]
        result += y
        result = ''.join(result)
        return result

    for k in input1:
        if input1[0] < k:
            resultlist.append(k)

    if len(resultlist) > 0:
        resultlist.sort()
        indeks = input1.index(resultlist[0])
        input1[0], input1[indeks] = input1[indeks], input1[0]
        y = input1[1:]
        y.sort()
        result = input1[:1]
        result += y
        result = ''.join(result)
        return result
    else:
        return ''