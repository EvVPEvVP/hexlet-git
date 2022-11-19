def Unmanned(L: int, N: int, track: list) -> int:

    if N == 1:
        result = track[0]
    if N == 1 and (result % (track[1] + track[2]) >= track[1]):
        result += L - track[0]
        return result
    if N == 1 and (result % (track[1] + track[2]) < track[1]):
        result += (track[1] - (result % (track[1] + track[2])))
        result += L - track[0]
        return result

    result = track[0][0]

    for i in range(len(track)):
        if (result % (track[i][1]+track[i][2])) < track[i][1]:
            result += (track[i][1] - (result % (track[i][1]+track[i][2])))
        if i != (len(track) - 1):
            result += (track[i+1][0] - track[i][0])
        if i == (len(track) - 1):
            result += L - track[i][0]
    return result







