def  MadMax(N: int, Tele: list) -> list:

    check = True
    while (check):
        check = False
        for i in range(N - 1):
            if Tele[i] > Tele[i + 1]:
                Tele[i], Tele[i + 1] = Tele[i + 1], Tele[i]
                check = True

    maks = max(Tele)
    maxindex = Tele.index(maks)
    middleindex = N // 2

    Tele[middleindex], Tele[maxindex] = Tele[maxindex], Tele[middleindex]

    check = True
    while (check):
        check = False
        for i in range(middleindex, len(Tele) - 1):
            if Tele[i] < Tele[i + 1]:
                Tele[i], Tele[i + 1] = Tele[i + 1], Tele[i]
                check = True
    return Tele