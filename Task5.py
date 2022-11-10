def SynchronizingTables(N: int, ids: list, salary: list) -> list:

    ids1 = []
    salary1 = []
    result = []

    for y in range(N):
        ids1.append(ids[y])
    for y1 in range(N):
        salary1.append(salary[y1])

    ids1.sort()
    salary1.sort()

    for i in ids:
        for x in ids1:
            if i == x:
                place = ids1.index(i)
                result.append(salary1[place])
    return result
