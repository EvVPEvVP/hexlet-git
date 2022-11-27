def SherlockValidString(s: str) -> bool:

    s1 = list(set(s))
    resultlist = []
    countmaxs = 0
    countmins = 0

    for i in s1:
        resultlist.append(s.count(i))

    mins = min(resultlist)
    maxs = max(resultlist)
    diff = maxs - mins

    for j in range(len(resultlist)):
        if maxs != resultlist[j]:
            countmaxs += 1
        if mins != resultlist[j]:
            countmins += 1
    if countmaxs == 1 and mins > 1 and len(resultlist) != 2:
        return False
    if diff <= 1 and (countmaxs <= 1 or countmins <= 1):
        return True
    return False