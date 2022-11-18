def UFO(N: int, data: list, octal: bool) -> list:

    ss = 16
    if octal == True:
        ss = 8
    result1 = []

    for j in data:
        strdata = str(j)
        result = 0
        count = 0
        for i in range(len(strdata)-1,-1,-1):
            result += int(strdata[count]) * (ss ** i)
            count += 1
        result1.append(result)

    return result1
