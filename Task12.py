def MassVote(N: int, votes: list) -> str:

    sum = 0
    perc = []
    count = 0
    result = ''
    maxindex = ''

    for i in votes:
        sum += i

    for i1 in votes:
        x = i1 / sum * 100
        perc.append(x)

    maxperc = max(perc)

    for i2 in range(len(perc)):
        if perc[i2] == maxperc:
            count += 1
            maxindex = str(i2 + 1)

    if count > 1:
        result = 'no winner'
    elif maxperc > 50:
        result = 'majority winner' + ' ' + maxindex
    else:
        result = 'minority winner' + ' ' + maxindex

    return result