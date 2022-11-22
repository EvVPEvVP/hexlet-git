def MisterRobot(N: int, data: list) -> bool:

    sortdata = list(data)
    sortdata.sort()
    count = 0

    while (data != sortdata):
        for i in range(0, N, 1):
            count = 0
            if i == (N - 2):
                break
            while data[i] > data[i+1] or data[i+1] > data[i+2]:
                count += 1
                data[i],data[i+1],data[i+2] = data[i+2],data[i],data[i+1]
                if count > 3:
                    return False
                if data == sortdata:
                    return True
